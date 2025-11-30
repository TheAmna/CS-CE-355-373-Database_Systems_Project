# database.py
import pyodbc

class Database:
    def __init__(self):
        self.server = r'DESKTOP-81TRJB1\SQLEXPRESS'
        self.database = 'TutorifyFinal'
        self.connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;'
    
    def get_connection(self):
        """Get a new database connection"""
        try:
            return pyodbc.connect(self.connection_string)
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            return None
    
    def execute_query(self, query, params=None):
        """Execute SELECT queries and return results"""
        conn = self.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                results = cursor.fetchall()
                return results
            except pyodbc.Error as e:
                print(f"Query error: {e}")
                return None
            finally:
                conn.close()
        return None
    
    def execute_update(self, query, params=None):
        """Execute INSERT, UPDATE, DELETE queries"""
        conn = self.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                return True
            except pyodbc.Error as e:
                print(f"Update error: {e}")
                conn.rollback()
                return False
            finally:
                conn.close()
        return False

# Test the database class
if __name__ == "__main__":
    db = Database()
    
    # Test 1: Get all tutors
    tutors = db.execute_query("SELECT * FROM Tutor")
    if tutors:
        print(f"[TUTORS] Found {len(tutors)} tutors")
        for tutor in tutors:
            print(f"  - {tutor}")
    else:
        print("[TUTORS] No tutors found or connection error")
    
    # Test 2: Get all students
    students = db.execute_query("SELECT * FROM Student")
    if students:
        print(f"[STUDENTS] Found {len(students)} students")
        for student in students:
            print(f"  - {student}")
    else:
        print("[STUDENTS] No students found or connection error")
    
    # Test 3: Get all subjects
    subjects = db.execute_query("SELECT * FROM Subject")
    if subjects:
        print(f"[SUBJECTS] Found {len(subjects)} subjects")
        for subject in subjects:
            print(f"  - {subject}")
    else:
        print("[SUBJECTS] No subjects found or connection error")
