# database.py
import pyodbc

class Database:
    def __init__(self):
        self.server = r'AMNA\MSSQLSERVER2022'
        self.database = 'Tutorify'
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

# Test the new database class
if __name__ == "__main__":
    db = Database()
    
    # Test 1: Get all tutors
    tutors = db.execute_query("SELECT * FROM Tutor")
    print("📚 Tutors:", len(tutors))
    
    # Test 2: Get all students
    students = db.execute_query("SELECT * FROM Student")
    print("🎓 Students:", len(students))
    
    # Test 3: Get all subjects
    subjects = db.execute_query("SELECT * FROM Subject")
    print("📖 Subjects:", len(subjects))