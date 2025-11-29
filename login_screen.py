# login_screen.py
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from database import Database

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        uic.loadUi('login.ui', self)
        
        # Connect buttons to functions
        self.btnLogin.clicked.connect(self.handle_login)
        
        # Show the window
        self.show()
    
    def handle_login(self):
        # Get form data
        email = self.lineEmail.text().strip()
        password = self.linePassword.text().strip()
        
        # Validation
        if not email or not password:
            QMessageBox.warning(self, "Error", "Please enter both email and password!")
            return
        
        # Check in database
        db = Database()
        
        # Check if user is a Student
        student = db.execute_query(
            "SELECT StudentID, Name FROM Student WHERE Email = ? AND Password = ?", 
            [email, password]
        )
        
        if student:
            student_id, student_name = student[0]
            QMessageBox.information(self, "Success", f"Welcome back, {student_name}!")
            self.open_student_dashboard(student_id, student_name)
            return
        
        # Check if user is a Tutor
        tutor = db.execute_query(
            "SELECT TutorID, Name FROM Tutor WHERE Email = ? AND Password = ?", 
            [email, password]
        )
        
        if tutor:
            tutor_id, tutor_name = tutor[0]
            QMessageBox.information(self, "Success", f"Welcome back, {tutor_name}!")
            # TODO: Open tutor dashboard when we create it
            QMessageBox.information(self, "Tutor Dashboard", "Tutor dashboard coming soon!")
            return
        
        # If no user found
        QMessageBox.warning(self, "Error", "Invalid email or password!")
    
    def open_student_dashboard(self, student_id, student_name):
        from student_dashboard import StudentDashboard
        self.dashboard = StudentDashboard(student_id, student_name)
        self.dashboard.show()
        self.hide()
