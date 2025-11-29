# student_dashboard.py
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QDateTime
from database import Database

class StudentDashboard(QtWidgets.QMainWindow):
    def __init__(self, student_id, student_name):
        super().__init__()
        
        # Load the UI file
        uic.loadUi('Student_dashboard.ui', self)
        
        # Store student info
        self.student_id = student_id
        self.student_name = student_name
        
        # DON'T change the title - keep it as "Student Dashboard"
        # Just setup the UI components
        self.setup_combo_level()
        self.setup_date_time()
        
        # Connect buttons
        self.btnBook.clicked.connect(self.schedule_session)
        self.btnViewResults_2.clicked.connect(self.view_sessions)
        
        # Load available tutors
        self.load_available_tutors()
        
        # Show the window
        self.show()
    
    def setup_combo_level(self):
        """Setup academic level options"""
        levels = ["Grade 9", "Grade 10", "Grade 11", "Grade 12", "O-Level", "A-Level", "University"]
        self.comboLevel.addItems(levels)
    
    def setup_date_time(self):
        """Setup date time picker - DON'T modify the appearance"""
        # Just set current date/time without changing UI
        current_datetime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(current_datetime)
    
    def load_available_tutors(self):
        """Load available tutors into the table"""
        db = Database()
        
        # Query to get tutors with their subjects and education
        query = """
        SELECT t.Name, s.Name, e.Education, '4.5' as Ratings
        FROM Tutor t
        JOIN TutorSubject ts ON t.TutorID = ts.TutorID
        JOIN Subject s ON ts.SubjectID = s.SubjectID
        JOIN Education e ON t.TutorID = e.TutorID
        """
        
        tutors = db.execute_query(query)
        
        # Clear existing rows
        self.tableTutors.setRowCount(0)
        
        # Populate table
        for row_index, tutor_data in enumerate(tutors):
            self.tableTutors.insertRow(row_index)
            for col_index, cell_data in enumerate(tutor_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableTutors.setItem(row_index, col_index, item)
    
    def schedule_session(self):
        """Schedule a new tutoring session"""
        subject = self.lineSubject.text().strip()
        level = self.comboLevel.currentText()
        datetime = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        
        # Validation
        if not subject:
            QMessageBox.warning(self, "Error", "Please enter a subject!")
            return
        
        # Get selected tutor
        selected_row = self.tableTutors.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a tutor from the table!")
            return
        
        tutor_name = self.tableTutors.item(selected_row, 0).text()
        tutor_subject = self.tableTutors.item(selected_row, 1).text()
        
        # Generate session ID
        db = Database()
        existing_sessions = db.execute_query("SELECT SessionID FROM Session")
        session_id = f"SESS{len(existing_sessions) + 1}"
        
        # Find the tutor ID
        available_tutors = db.execute_query("SELECT TutorID FROM Tutor WHERE Name = ?", [tutor_name])
        if available_tutors:
            tutor_id = available_tutors[0][0]
            
            # Find the subject ID
            subject_data = db.execute_query("SELECT SubjectID FROM Subject WHERE Name = ?", [tutor_subject])
            if subject_data:
                subject_id = subject_data[0][0]
            else:
                # Use default subject if not found
                subject_id = "SUB1"
            
            # Insert session
            success = db.execute_update(
                """INSERT INTO Session (SessionID, DateTime, Status, TutorID, StudentID, SubjectID) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                [session_id, datetime, "Pending", tutor_id, self.student_id, subject_id]
            )
            
            if success:
                QMessageBox.information(self, "Success", 
                                      f"Session scheduled successfully!\n"
                                      f"Tutor: {tutor_name}\n"
                                      f"Subject: {subject}\n"
                                      f"Level: {level}\n"
                                      f"Date: {datetime}")
                
                # Clear the subject field after successful booking
                self.lineSubject.clear()
            else:
                QMessageBox.critical(self, "Error", "Failed to schedule session!")
        else:
            QMessageBox.warning(self, "Error", "Selected tutor not found!")
    
    def view_sessions(self):
        """View student's scheduled sessions"""
        db = Database()
        
        sessions = db.execute_query(
            """SELECT s.SessionID, s.DateTime, s.Status, t.Name as TutorName, sub.Name as SubjectName
            FROM Session s
            JOIN Tutor t ON s.TutorID = t.TutorID
            JOIN Subject sub ON s.SubjectID = sub.SubjectID
            WHERE s.StudentID = ?""",
            [self.student_id]
        )
        
        if sessions:
            session_info = "Your Scheduled Sessions:\n\n"
            for session in sessions:
                session_id, datetime, status, tutor_name, subject_name = session
                session_info += f"{subject_name} with {tutor_name}\n"
                session_info += f"Date: {datetime}\n"
                session_info += f"Status: {status}\n"
                session_info += f"Session ID: {session_id}\n\n"
            
            QMessageBox.information(self, "Your Sessions", session_info)
        else:
            QMessageBox.information(self, "Sessions", "No sessions scheduled yet!")


# Test the student dashboard
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # For testing, provide sample student data
    window = StudentDashboard("S1", "Test Student")
    sys.exit(app.exec())