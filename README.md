

# CS-CE-355-373-Database-Systems-Project

## Team Members 
- [Amna Ali](https://github.com/TheAmna)
- [Humna Khan](https://github.com/humna0809)

## Project Description

Our project Tutorify is a community-driven online tutoring platform in Pakistan. It aims to address the need for a platform that connects students with qualified tutors. Traditional method of finding tutors can be time-consuming. Hence, Tutorify is designed to bridge this gap by creating a desktop-based GUI for students seeking academic help, tutors looking for teaching opportunities.

## Functional Requirements 

-User Types:

	User A : Student 
	User B : Tutor
  
- Module 1: Register and login

	The system shall allow Students and Tutors to register an account and login.
  
- Module 2: Student Dashboard to search for tutor and view available tutors.

	The system shall allow Student to enter requirement and search for tutor.
  
- Module 3: Tutor Dashboard to view profile and approve or complete sessions.

    The system shall allow tutors to access their profile and manage sessions.
  
- Module 4: Session Management for both students and tutors.

	The system shall allow both the Student and Tutor to see session status.
  
- Module 5: Feedback Form for students.

	The system shall allow students to submit feedback




## Entity Relationship Diagram 

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/b2907013-d5aa-4b38-add8-581a02c5c35a" />




## Relation Schema 


<img width="900" height="700" alt="Screenshot 2025-11-09 143047" src="https://github.com/user-attachments/assets/857872d2-09c1-4268-a717-d8b530f10ad6" />



## Graphical User Interface (GUI)



### Welcome screen

<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/c472a148-706e-43e7-8f5f-314064ece296" />

*Screen 1A : The system allows both student and tutor to choose to login or signup.*


### Create Account

<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/b96d3952-048e-42bf-8053-e0479b183359" />

*Screen 1B : The system allows both student and tutor to create an account first.*

### Login 

<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/acc07efa-1494-4b5f-b359-a154678f4037" />

*Screen 1C : The system allows both student and tutor to login after creating an account.*

### Student Dashboard  

<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/28129fd3-f36c-47b0-820b-bbd7e67b906b" />

*Screen 2A : Allows student to add search details, then view the search results to schedule session with tutor.*

### Tutor Dashboard

<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/f0ffa1ba-9dd0-465b-adb7-55da6285a454" />

*Screen 3A : Allows tutor to view & update profile. Also allows to approves requested sessions from students.*

### Session Management 

<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/52194703-a584-43d7-8661-1201e3e9db75" />

*Screen 4A : Allows students and tutors to view the status of the scheduled sessions. Status can be ‘approved’, ‘pending’, ‘completed’.*


### Feedback Form 


<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/888be2ea-a22e-4ab8-9d12-f60d49f0c41a" />


*Screen 5A : Allows students and tutors to give feedback after scheduled session takes place. Completes cycle.*



## Structured Query Language (SQL)

SQL Query 1.B:  Register a new Student

```
INSERT INTO Student (StudentID , Name, Email, Password, CNIC)
VALUES (‘S001’, ‘Aliza Ali’, ‘hahaha’, ‘aa02&gmail.com’, ‘42101-1234567-1');
```

SQL Query 1.B.2:  Register a new Tutor

```
INSERT INTO Tutor (TutorID, Name, Email, Password, Education, Experience, CNIC)
VALUES ('T001', 'Amna Khan', 'ak02@gmail.com', '1234ak', 'BCOM', '2', '42101-1234567-2');
```

SQL Query 1.C.1:  Student login verification

```
SELECT StudentID, Name, Email, CNIC
FROM Student s
WHERE s.Email = ’aa02@gmail.com’ and s.Password= ’hahaha’;
```

SQL Query 1.C.2:  Tutor login verification
```
SELECT TutorID, Name, Email, Password, Education, Experience, CNIC
FROM Tutor t
WHERE t.Email= ‘ak02&gmail.com’ and t.Password= ‘1234ak’;
```

SQL QUERY 2.A.1: When user clicks View Results the table is filtered out based on subject
```

 		SELECT t.TutorID, t.Name as TutorName, s.Name as Subject, e.Education,  				ISNULL(ROUND(AVG(CAST(f.Rating AS FLOAT)), 2), 0) as Rating
FROM Tutor t 
INNER JOIN TutorSubject ts ON t.TutorID = ts.TutorID 
INNER JOIN Subject s ON 	ts.SubjectID = s.SubjectID
 LEFT JOIN Education e ON t.TutorID = e.TutorID 
LEFT JOIN Feedback 	f ON t.TutorID = f.TutorID
WHERE  s.Name LIKE '%' + @SubjectName + '%'
GROUP BY t.TutorID, t.Name, s.Name,  e.Education, t.Experience
ORDER BY Rating DESC,t.Name;
````

SQL Query 2.A.2:  When user clicks Schedule button. This books a new session with the selected tutor based on inputs from the dashboard

```
INSERT INTO Sessions (session_id,student_id, tutor_id, subject_id, date/time, status) 
VALUES (.’s001’, ‘ak09873’, ‘t124’, ‘core101’, GETDATE(), 'Pending')
```

SQL Query 3.A.1: View Tutor Profile 

```
SELECT t.TutorID, t.Name,  t.Experience,  e.Education, STRING_AGG(s.Name, ', ') as Subjects 
FROM Tutor t LEFT
 JOIN Education e ON t.TutorID = e.TutorID
 LEFT JOIN TutorSubject ts ON t.TutorID = ts.TutorID
 LEFT JOIN Subject s ON ts.SubjectID = s.SubjectID WHERE t.TutorID = 'T001' 
GROUP BY t.TutorID, t.Name, t.Email, t.Experience, t.CNIC, e.Education;
```

SQL Query 3.A.2: Update Tutor Name

```
UPDATE Tutor
SET Name = 'Amna Khan Updated' WHERE TutorID = 'T001';
```
SQL Query 3.A.3: Update Tutor Experience 	

```
UPDATE Tutor
SET Experience = '3 years' WHERE TutorID = 'T001';
```

SQL Query 3.A.4: Update Tutor Education 
```
UPDATE Education
SET Education = 'BCS' WHERE TutorID = 'T001';
```

SQL Query 3.B.1: View Pending Session Requests 
```
SELECT s.SessionID , T.Name as TutorName , S.Name as StudentName , sub.Name as Subject , s.Date/time , s.Status
FROM Session s
 JOIN Tutor t ON t.TutorID = s.TutorID 
JOIN Student st ON st.StudentID = s.SessionID 
 JOIN Subject sub ON sub.SubjectID = s.SubjectID 
WHERE s.Status = ‘Pending’
```

SQL Query 3.B.2: Approve Session Request 
```

UPDATE Session
SET Status = 'Approved' 
WHERE SessionID = 'SES001' AND TutorID = 'T001' AND Status = 'Pending'
```

SQL Query 3.B.3: Reject/Disapprove Session Request 
```
UPDATE Session 
SET Status = 'Rejected'
WHERE SessionID = 'SES001' AND TutorID = 'T001' AND Status = 'Pending'
```



SQL Query 4.A.1: This query looks for  all scheduled sessions for the current tutor to populate the tableSessions 
```
SELECT t.full_name AS Tutor_Name, s.full_name AS Student_Name, ses.subject, ses.session_date AS Date, ses.time_slot, ses.hours, ses.status
 FROM Sessions ses INNER JOIN Tutors t ON ses.tutor_id = t.tutor_id 
INNER JOIN Students s ON ses.student_id = s.student_id 
WHERE ses.tutor_id = ‘t1324’
ORDER BY ses.session_date DESC
```

SQL Query 4.A.2: updates the status of past sessions to 'Completed'
```
UPDATE Sessions 
SET status = 'Completed' 
WHERE session_id = ‘hk908’ AND status = 'Pending' AND session_date < GETDATE()
```

SQL Query 5.A.1: Inserts the new feedback record with rating and comment (e.g., for session 123, student 456, tutor 789)
```
INSERT INTO Feedback (session_id, student_id, tutor_id, rating, comment) 
VALUES (‘s123’, ‘aa456’, ‘t789’, 4, 'Good')
```

SQL Query 5.A.2:  Updates the tutor's average rating
```
UPDATE Tutors
SET average_rating =   (SELECT AVG(rating)
						FROM Feedback
						WHERE tutor_id = 789)
WHERE tutor_id = 789
```












