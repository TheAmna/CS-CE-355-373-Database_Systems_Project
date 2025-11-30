# # # student_dashboard.py
# # from PyQt6 import QtWidgets, uic
# # from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
# # from PyQt6.QtCore import QDateTime
# # from database import Database

# # class StudentDashboard(QtWidgets.QMainWindow):
# #     def __init__(self, student_id, student_name):
# #         super().__init__()
        
# #         # Load the UI file
# #         uic.loadUi('Student_dashboard.ui', self)
        
# #         # Store student info
# #         self.student_id = student_id
# #         self.student_name = student_name
        
# #         # DON'T change the title - keep it as "Student Dashboard"
# #         # Just setup the UI components
# #         self.setup_combo_level()
# #         self.setup_date_time()
        
# #         # Connect buttons
# #         self.btnBook.clicked.connect(self.schedule_session)
# #         self.btnViewResults_2.clicked.connect(self.view_sessions)
        
# #         # Load available tutors
# #         self.load_available_tutors()
        
# #         # Show the window
# #         self.show()
    
# #     def setup_combo_level(self):
# #         """Setup academic level options"""
# #         levels = ["Grade 9", "Grade 10", "Grade 11", "Grade 12", "O-Level", "A-Level", "University"]
# #         self.comboLevel.addItems(levels)
    
# #     def setup_date_time(self):
# #         """Setup date time picker - DON'T modify the appearance"""
# #         # Just set current date/time without changing UI
# #         current_datetime = QDateTime.currentDateTime()
# #         self.dateTimeEdit.setDateTime(current_datetime)
    
# #     def load_available_tutors(self):
# #         """Load available tutors into the table"""
# #         db = Database()
        
# #         # Query to get tutors with their subjects and education
# #         query = """
# #         SELECT t.Name, s.Name, e.Education, '4.5' as Ratings
# #         FROM Tutor t
# #         JOIN TutorSubject ts ON t.TutorID = ts.TutorID
# #         JOIN Subject s ON ts.SubjectID = s.SubjectID
# #         JOIN Education e ON t.TutorID = e.TutorID
# #         """
        
# #         tutors = db.execute_query(query)
        
# #         # Clear existing rows
# #         self.tableTutors.setRowCount(0)
        
# #         # Populate table
# #         for row_index, tutor_data in enumerate(tutors):
# #             self.tableTutors.insertRow(row_index)
# #             for col_index, cell_data in enumerate(tutor_data):
# #                 item = QTableWidgetItem(str(cell_data))
# #                 self.tableTutors.setItem(row_index, col_index, item)
    
# #     def schedule_session(self):
# #         """Schedule a new tutoring session"""
# #         subject = self.lineSubject.text().strip()
# #         level = self.comboLevel.currentText()
# #         datetime = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        
# #         # Validation
# #         if not subject:
# #             QMessageBox.warning(self, "Error", "Please enter a subject!")
# #             return
        
# #         # Get selected tutor
# #         selected_row = self.tableTutors.currentRow()
# #         if selected_row == -1:
# #             QMessageBox.warning(self, "Error", "Please select a tutor from the table!")
# #             return
        
# #         tutor_name = self.tableTutors.item(selected_row, 0).text()
# #         tutor_subject = self.tableTutors.item(selected_row, 1).text()
        
# #         # Generate session ID
# #         db = Database()
# #         existing_sessions = db.execute_query("SELECT SessionID FROM Session")
# #         session_id = f"SESS{len(existing_sessions) + 1}"
        
# #         # Find the tutor ID
# #         available_tutors = db.execute_query("SELECT TutorID FROM Tutor WHERE Name = ?", [tutor_name])
# #         if available_tutors:
# #             tutor_id = available_tutors[0][0]
            
# #             # Find the subject ID
# #             subject_data = db.execute_query("SELECT SubjectID FROM Subject WHERE Name = ?", [tutor_subject])
# #             if subject_data:
# #                 subject_id = subject_data[0][0]
# #             else:
# #                 # Use default subject if not found
# #                 subject_id = "SUB1"
            
# #             # Insert session
# #             success = db.execute_update(
# #                 """INSERT INTO Session (SessionID, DateTime, Status, TutorID, StudentID, SubjectID) 
# #                 VALUES (?, ?, ?, ?, ?, ?)""",
# #                 [session_id, datetime, "Pending", tutor_id, self.student_id, subject_id]
# #             )
            
# #             if success:
# #                 QMessageBox.information(self, "Success", 
# #                                       f"Session scheduled successfully!\n"
# #                                       f"Tutor: {tutor_name}\n"
# #                                       f"Subject: {subject}\n"
# #                                       f"Level: {level}\n"
# #                                       f"Date: {datetime}")
                
# #                 # Clear the subject field after successful booking
# #                 self.lineSubject.clear()
# #             else:
# #                 QMessageBox.critical(self, "Error", "Failed to schedule session!")
# #         else:
# #             QMessageBox.warning(self, "Error", "Selected tutor not found!")
    
# #     def view_sessions(self):
# #         """View student's scheduled sessions"""
# #         db = Database()
        
# #         sessions = db.execute_query(
# #             """SELECT s.SessionID, s.DateTime, s.Status, t.Name as TutorName, sub.Name as SubjectName
# #             FROM Session s
# #             JOIN Tutor t ON s.TutorID = t.TutorID
# #             JOIN Subject sub ON s.SubjectID = sub.SubjectID
# #             WHERE s.StudentID = ?""",
# #             [self.student_id]
# #         )
        
# #         if sessions:
# #             session_info = "Your Scheduled Sessions:\n\n"
# #             for session in sessions:
# #                 session_id, datetime, status, tutor_name, subject_name = session
# #                 session_info += f"{subject_name} with {tutor_name}\n"
# #                 session_info += f"Date: {datetime}\n"
# #                 session_info += f"Status: {status}\n"
# #                 session_info += f"Session ID: {session_id}\n\n"
            
# #             QMessageBox.information(self, "Your Sessions", session_info)
# #         else:
# #             QMessageBox.information(self, "Sessions", "No sessions scheduled yet!")


# # # Test the student dashboard
# # if __name__ == "__main__":
# #     import sys
# #     app = QtWidgets.QApplication(sys.argv)
# #     # For testing, provide sample student data
# #     window = StudentDashboard("S1", "Test Student")
# #     sys.exit(app.exec())
# student_dashboard.py
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt6.QtCore import QDateTime
from database import Database

class StudentDashboard(QtWidgets.QMainWindow):
    def __init__(self, student_id, student_name):
        super().__init__()
        
        # Store student info
        self.student_id = student_id
        self.student_name = student_name
        
        # Load the UI file
        uic.loadUi('Student_dashboard.ui', self)
        
        # Fix text color for input fields
        self.fix_text_colors()
        
        # Initialize UI components
        self.initialize_ui()
        
        # Connect buttons to functions
        self.connect_signals()
        
        # Load initial data
        self.load_initial_data()
        
        # Show the window
        self.show()
    
    def fix_text_colors(self):
        """Fix text color visibility for all input fields"""
        self.lineSubject.setStyleSheet("color: black;")
        self.comboLevel.setStyleSheet("color: black;")
        self.dateTimeEdit.setStyleSheet("color: black;")
        
    def initialize_ui(self):
        """Initialize UI components with default values"""
        # Set current date and time
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        # Populate academic level combo box
        levels = ["Primary School", "Middle School", "High School", 
                 "O-Levels", "A-Levels", "Undergraduate", "Graduate"]
        self.comboLevel.addItems(levels)
        
        # Set window title with student name
        self.setWindowTitle(f"Tutorify - {self.student_name}'s Dashboard")
    
    def connect_signals(self):
        """Connect all buttons to their respective functions"""
        self.btnViewResults.clicked.connect(self.handle_view_results)
        self.btnBook.clicked.connect(self.handle_schedule_session)
        self.btnViewResults_2.clicked.connect(self.handle_view_sessions)
        
        # Connect search functionality
        self.lineSubject.textChanged.connect(self.search_tutors)
        self.comboLevel.currentTextChanged.connect(self.search_tutors)
    
    def load_initial_data(self):
        """Load initial data into the dashboard"""
        # Load available tutors
        self.search_tutors()
        
        # Display welcome message
        QMessageBox.information(self, "Welcome", 
                              f"Welcome back, {self.student_name}!\nStudent ID: {self.student_id}")
    
    def search_tutors(self):
        """Search for tutors based on subject and level"""
        subject = self.lineSubject.text().strip()
        level = self.comboLevel.currentText()
        
        db = Database()
        
        # Build query based on search criteria
        if subject:
            query = """
                SELECT t.Name, s.SubjectName, t.Education, t.Rating 
                FROM Tutor t
                LEFT JOIN TutorSubjects ts ON t.TutorID = ts.TutorID
                LEFT JOIN Subject s ON ts.SubjectID = s.SubjectID
                WHERE s.SubjectName LIKE ? OR t.Name LIKE ?
            """
            params = [f'%{subject}%', f'%{subject}%']
        else:
            query = """
                SELECT t.Name, s.SubjectName, t.Education, t.Rating 
                FROM Tutor t
                LEFT JOIN TutorSubjects ts ON t.TutorID = ts.TutorID
                LEFT JOIN Subject s ON ts.SubjectID = s.SubjectID
            """
            params = []
        
        tutors = db.execute_query(query, params)
        
        # Populate the table
        self.populate_tutors_table(tutors)
    
    def populate_tutors_table(self, tutors):
        """Populate the tutors table with data"""
        self.tableTutors.setRowCount(0)  # Clear existing rows
        
        if not tutors:
            self.tableTutors.setRowCount(1)
            self.tableTutors.setItem(0, 0, QTableWidgetItem("No tutors found"))
            return
        
        self.tableTutors.setRowCount(len(tutors))
        
        for row, tutor in enumerate(tutors):
            name, subject, education, rating = tutor
            rating = rating if rating else "No ratings yet"
            education = education if education else "Not specified"
            subject = subject if subject else "General"
            
            self.tableTutors.setItem(row, 0, QTableWidgetItem(str(name)))
            self.tableTutors.setItem(row, 1, QTableWidgetItem(str(subject)))
            self.tableTutors.setItem(row, 2, QTableWidgetItem(str(education)))
            self.tableTutors.setItem(row, 3, QTableWidgetItem(str(rating)))
    
    def handle_view_results(self):
        """Handle View Results button click"""
        subject = self.lineSubject.text().strip()
        
        if not subject:
            QMessageBox.warning(self, "Search Required", 
                              "Please enter a subject to view available tutors!")
            return
        
        self.search_tutors()
        QMessageBox.information(self, "Search Complete", 
                              f"Found tutors for: {subject}")
    
    def handle_schedule_session(self):
        """Handle Schedule Session button click"""
        selected_row = self.tableTutors.currentRow()
        
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Required", 
                              "Please select a tutor from the table!")
            return
        
        # Get selected tutor info
        tutor_name = self.tableTutors.item(selected_row, 0).text()
        subject = self.tableTutors.item(selected_row, 1).text()
        session_datetime = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        
        # Get tutor ID from database
        db = Database()
        tutor_result = db.execute_query(
            "SELECT TutorID FROM Tutor WHERE Name = ?", 
            [tutor_name]
        )
        
        if not tutor_result:
            QMessageBox.warning(self, "Error", "Could not find tutor details!")
            return
        
        tutor_id = tutor_result[0][0]
        
        # Insert session into database
        success = db.execute_update(
            """INSERT INTO Sessions (StudentID, TutorID, Subject, SessionDateTime, Status) 
               VALUES (?, ?, ?, ?, ?)""",
            [self.student_id, tutor_id, subject, session_datetime, "Scheduled"]
        )
        
        if success:
            QMessageBox.information(self, "Session Scheduled", 
                                  f"Session with {tutor_name} scheduled for {session_datetime}!")
            self.clear_form()
        else:
            QMessageBox.critical(self, "Error", "Failed to schedule session. Please try again.")
    
    def handle_view_sessions(self):
        """Handle View Sessions button click"""
        db = Database()
        
        sessions = db.execute_query(
            """SELECT s.SessionID, t.Name, s.Subject, s.SessionDateTime, s.Status 
               FROM Sessions s
               JOIN Tutor t ON s.TutorID = t.TutorID
               WHERE s.StudentID = ?
               ORDER BY s.SessionDateTime DESC""",
            [self.student_id]
        )
        
        if not sessions:
            QMessageBox.information(self, "No Sessions", 
                                  "You haven't scheduled any sessions yet!")
            return
        
        # Create sessions summary
        session_text = "Your Scheduled Sessions:\n\n"
        for session in sessions:
            session_id, tutor_name, subject, datetime, status = session
            session_text += f"• {tutor_name} - {subject}\n"
            session_text += f"  Date: {datetime} | Status: {status}\n\n"
        
        QMessageBox.information(self, "Your Sessions", session_text)
    
    def clear_form(self):
        """Clear the search form"""
        self.lineSubject.clear()
        self.comboLevel.setCurrentIndex(0)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.tableTutors.setRowCount(0)

# Test the student dashboard
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Test with sample student data
    window = StudentDashboard("S1", "Test Student")
    sys.exit(app.exec())

# import sys
# import sqlite3
# from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
# from PyQt6.QtCore import QDateTime
# from PyQt6.uic import loadUi

# class StudentDashboard(QWidget):
#     def __init__(self):
#         super().__init__()
#         # Load the UI file
#         loadUi('Student_dashboard.ui', self)
        
#         # Connect to existing database
#         self.conn = sqlite3.connect('TutorifyDatabase.db')
#         self.cursor = self.conn.cursor()
        
#         # Populate academic level dropdown
#         self.populate_academic_levels()
        
#         # Connect signals to slots
#         self.btnViewResults_2.clicked.connect(self.view_sessions)
#         self.btnBook.clicked.connect(self.schedule_session)
        
#         # Set minimum datetime to current time
#         self.dateTimeEdit.setMinimumDateTime(QDateTime.currentDateTime())
    
#     def populate_academic_levels(self):
#         """Populate the academic level dropdown from database"""
#         try:
#             self.cursor.execute("SELECT DISTINCT academic_level FROM Tutors")
#             levels = self.cursor.fetchall()
            
#             self.comboLevel.clear()
#             for level in levels:
#                 self.comboLevel.addItem(level[0])
#         except Exception as e:
#             print(f"Error loading academic levels: {e}")

#     def view_sessions(self):
#         """Show available tutoring sessions based on subject and datetime"""
#         subject = self.lineSubject.text().strip()
#         academic_level = self.comboLevel.currentText()
#         selected_datetime = self.dateTimeEdit.dateTime()
        
#         if not subject:
#             QMessageBox.warning(self, "Input Error", "Please enter a subject/course.")
#             return
        
#         if not academic_level:
#             QMessageBox.warning(self, "Input Error", "Please select an academic level.")
#             return
        
#         # Convert QDateTime to Python format
#         py_datetime = selected_datetime.toPyDateTime()
#         selected_date = py_datetime.strftime('%Y-%m-%d')
#         selected_time = py_datetime.strftime('%H:%M:%S')
        
#         try:
#             # Query for available tutors for the selected subject, level and time slot
#             query = """
#             SELECT t.tutor_name, t.subject, t.education, t.rating, 
#                    a.available_date, a.start_time, a.end_time, a.availability_id
#             FROM Tutors t
#             JOIN Availability a ON t.tutor_id = a.tutor_id
#             WHERE t.subject LIKE ? 
#             AND t.academic_level = ?
#             AND a.available_date = ?
#             AND a.start_time <= ? 
#             AND a.end_time > ?
#             AND a.is_booked = 0
#             """
            
#             self.cursor.execute(query, (f'%{subject}%', academic_level, selected_date, selected_time, selected_time))
#             available_tutors = self.cursor.fetchall()
            
#             # Clear the table
#             self.tableTutors.setRowCount(0)
            
#             if not available_tutors:
#                 QMessageBox.information(self, "No Sessions", 
#                                       "No available tutoring sessions found for the selected criteria.")
#                 return
            
#             # Populate the table with available sessions
#             for row, tutor in enumerate(available_tutors):
#                 self.tableTutors.insertRow(row)
                
#                 # Display tutor information
#                 self.tableTutors.setItem(row, 0, QTableWidgetItem(tutor[0]))  # Tutor Name
#                 self.tableTutors.setItem(row, 1, QTableWidgetItem(tutor[1]))  # Subject
#                 self.tableTutors.setItem(row, 2, QTableWidgetItem(tutor[2]))  # Education
#                 self.tableTutors.setItem(row, 3, QTableWidgetItem(str(tutor[3])))  # Ratings
                
#                 # Store availability_id in hidden data (column 4)
#                 self.tableTutors.setItem(row, 4, QTableWidgetItem(str(tutor[7])))
                
#         except Exception as e:
#             QMessageBox.critical(self, "Database Error", f"Error loading sessions: {str(e)}")

#     def schedule_session(self):
#         """Schedule a session with the selected tutor"""
#         current_row = self.tableTutors.currentRow()
        
#         if current_row == -1:
#             QMessageBox.warning(self, "Selection Error", "Please select a tutor from the table.")
#             return
        
#         try:
#             # Get the selected availability_id from hidden column
#             availability_id = int(self.tableTutors.item(current_row, 4).text())
#             tutor_name = self.tableTutors.item(current_row, 0).text()
#             subject = self.lineSubject.text().strip()
#             academic_level = self.comboLevel.currentText()
#             selected_datetime = self.dateTimeEdit.dateTime().toPyDateTime()
            
#             # Get student_id (assuming student is logged in, using 1 for demo)
#             student_id = 1
            
#             # Get tutor_id from availability
#             self.cursor.execute("SELECT tutor_id FROM Availability WHERE availability_id = ?", (availability_id,))
#             tutor_id = self.cursor.fetchone()[0]
            
#             # Insert into Sessions table
#             self.cursor.execute("""
#                 INSERT INTO Sessions (student_id, tutor_id, subject, academic_level, session_date, session_time, status)
#                 VALUES (?, ?, ?, ?, ?, ?, 'Scheduled')
#             """, (student_id, tutor_id, subject, academic_level, 
#                   selected_datetime.strftime('%Y-%m-%d'), 
#                   selected_datetime.strftime('%H:%M:%S')))
            
#             # Update availability as booked
#             self.cursor.execute("UPDATE Availability SET is_booked = 1 WHERE availability_id = ?", (availability_id,))
            
#             self.conn.commit()
            
#             QMessageBox.information(self, "Success", 
#                                   f"Session scheduled successfully with {tutor_name}!")
            
#             # Refresh the available sessions
#             self.view_sessions()
            
#         except Exception as e:
#             self.conn.rollback()
#             QMessageBox.critical(self, "Database Error", f"Error scheduling session: {str(e)}")

#     def closeEvent(self, event):
#         """Close database connection when window is closed"""
#         self.conn.close()
#         event.accept()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = StudentDashboard()
#     window.show()
#     sys.exit(app.exec())
