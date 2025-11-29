# signup_screen.py
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from database import Database
import re

class SignupScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        uic.loadUi('signup_fixed.ui', self)
        
        # Connect buttons to functions
        self.btnSignup.clicked.connect(self.handle_signup)
        
        # Show the window
        self.show()
    
    def validate_email(self, email):
        """Simple email validation"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_cnic(self, cnic):
        """Validate CNIC format (simple check)"""
        return len(cnic) >= 13 and cnic.isdigit()
    
    def generate_user_id(self, role):
        """Generate unique user ID (T1, T2, S1, S2, etc.)"""
        db = Database()
        
        if role == "Tutor":
            existing_tutors = db.execute_query("SELECT TutorID FROM Tutor")
            next_number = len(existing_tutors) + 1
            return f"T{next_number}"
        else:  # Student
            existing_students = db.execute_query("SELECT StudentID FROM Student")
            next_number = len(existing_students) + 1
            return f"S{next_number}"
    
    def handle_signup(self):
        # Get form data
        name = self.lineName.text().strip()
        email = self.lineEmail.text().strip()
        password = self.linePassword.text().strip()
        cnic = self.lineCNIC.text().strip()  # CNIC field
        role = self.comboRole.currentText()
        
        # Validation
        if not name or not email or not password or not cnic:
            QMessageBox.warning(self, "Error", "Please fill all fields!")
            return
        
        if not self.validate_email(email):
            QMessageBox.warning(self, "Error", "Please enter a valid email address!")
            return
        
        if not self.validate_cnic(cnic):
            QMessageBox.warning(self, "Error", "CNIC must be at least 13 digits!")
            return
        
        # Check if email already exists
        db = Database()
        
        if role == "Tutor":
            existing_tutor = db.execute_query("SELECT TutorID FROM Tutor WHERE Email = ?", [email])
            if existing_tutor:
                QMessageBox.warning(self, "Error", "Email already registered as Tutor!")
                return
        else:  # Student
            existing_student = db.execute_query("SELECT StudentID FROM Student WHERE Email = ?", [email])
            if existing_student:
                QMessageBox.warning(self, "Error", "Email already registered as Student!")
                return
        
        # Generate user ID and insert into database
        user_id = self.generate_user_id(role)
        
        if role == "Tutor":
            success = db.execute_update(
                "INSERT INTO Tutor (TutorID, Name, Email, Password, CNIC) VALUES (?, ?, ?, ?, ?)",
                [user_id, name, email, password, cnic]
            )
        else:  # Student
            success = db.execute_update(
                "INSERT INTO Student (StudentID, Name, Email, Password, CNIC) VALUES (?, ?, ?, ?, ?)",
                [user_id, name, email, password, cnic]
            )
        
        if success:
            QMessageBox.information(self, "Success", 
                                  f"Account created successfully!\nYour {role} ID: {user_id}")
            self.close()  # Close signup window
            # TODO: Open login screen or homepage
        else:
            QMessageBox.critical(self, "Error", "Failed to create account. Please try again.")

# Test the signup screen
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SignupScreen()
    sys.exit(app.exec())