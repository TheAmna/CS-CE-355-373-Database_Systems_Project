# homepage.py
from PyQt6 import QtWidgets, uic
import sys

class HomePage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the UI file
        uic.loadUi('tutorifyhomepage.ui', self)
        
        # Connect buttons to functions
        self.btnLogin.clicked.connect(self.open_login)
        self.btnSignup.clicked.connect(self.open_signup)
        
        # Show the window
        self.show()
    
    def open_login(self):
        from login_screen import LoginScreen
        self.login_window = LoginScreen()
        self.login_window.show()
        self.hide()
    
    def open_signup(self):
        from signup_screen import SignupScreen
        self.signup_window = SignupScreen()
        self.signup_window.show()
        self.hide()

# Main application
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HomePage()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
