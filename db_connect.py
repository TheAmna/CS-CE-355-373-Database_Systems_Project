# test_connection.py
import pyodbc

def test_tutorify_connection():
    try:
        # Use the same connection string from your previous lab
        server = r'AMNA\MSSQLSERVER2022'
        database = 'TutorifyDatabase'
        
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        
        print("🔌 Attempting to connect to Tutorify database...")
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        # Test query - get all tutors
        cursor.execute("SELECT TutorID, Name, Email FROM Tutor")
        tutors = cursor.fetchall()
        
        print("✅ SUCCESS: Connected to Tutorify database!")
        print(f"📊 Found {len(tutors)} tutors in database:")
        
        for tutor in tutors:
            print(f"   - {tutor.TutorID}: {tutor.Name} ({tutor.Email})")
        
        # Close connection
        cursor.close()
        connection.close()
        print("🔒 Connection closed properly")
        
        return True
        
    except pyodbc.Error as e:
        print(f"❌ ERROR: Failed to connect to database")
        print(f"Error details: {e}")
        return False

if __name__ == "__main__":
    test_tutorify_connection()
