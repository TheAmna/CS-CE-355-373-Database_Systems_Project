-- CREATE DATABASE Tutorify;
-- GO

-- USE Tutorify;
-- GO


-- CREATE TABLE Tutor (
--     TutorID      VARCHAR(50) PRIMARY KEY,
--     Name         VARCHAR(50),
--     Email        VARCHAR(50),
--     Password     VARCHAR(50),
--     CNIC         VARCHAR(20)
-- );


-- CREATE TABLE Student (
--     StudentID    VARCHAR(50) PRIMARY KEY,
--     Name         VARCHAR(50),
--     Email        VARCHAR(50),
--     Password     VARCHAR(50),
--     CNIC         VARCHAR(20)
-- );


-- CREATE TABLE Subject (
--     SubjectID      VARCHAR(50) PRIMARY KEY,
--     Name           VARCHAR(50),
--     AcademicLevel  VARCHAR(50)
-- );


-- CREATE TABLE Education (
--     EduID      INT IDENTITY(1,1) PRIMARY KEY,
--     TutorID    VARCHAR(50),
--     Education  VARCHAR(50),
--     FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID)
-- );


-- CREATE TABLE TutorStudent (
--     TutorID    VARCHAR(50),
--     StudentID  VARCHAR(50),
--     PRIMARY KEY (TutorID, StudentID),
--     FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
-- );

-- CREATE TABLE TutorSubject (
--     TutorID    VARCHAR(50),
--     SubjectID  VARCHAR(50),
--     PRIMARY KEY (TutorID, SubjectID),
--     FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
--     FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
-- );


-- CREATE TABLE StudentSubject (
--     StudentID  VARCHAR(50),
--     SubjectID  VARCHAR(50),
--     PRIMARY KEY (StudentID, SubjectID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
--     FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
-- );


-- CREATE TABLE Session (
--     SessionID   VARCHAR(50) PRIMARY KEY,
--     DateTime    DATETIME,
--     Status      VARCHAR(20),
--     TutorID     VARCHAR(50),
--     StudentID   VARCHAR(50),
--     SubjectID   VARCHAR(50),
--     FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
--     FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
-- );


-- CREATE TABLE Feedback (
--     FeedbackID  VARCHAR(50) PRIMARY KEY,
--     Rating      INT,
--     Comment     VARCHAR(50),
--     TutorID     VARCHAR(50),
--     StudentID   VARCHAR(50),
--     SessionID   VARCHAR(50),
--     FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
--     FOREIGN KEY (SessionID) REFERENCES Session(SessionID)
-- );
-- Create a new database
CREATE DATABASE TutorifyDatabase;
GO

USE TutorifyDatabase;
GO

-- 1. Tutor Table
CREATE TABLE Tutor (
    TutorID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(50),
    Password VARCHAR(50),
    Education VARCHAR(100),
    Experience VARCHAR(100),
    CNIC VARCHAR(20)
);

-- 2. Student Table
CREATE TABLE Student (
    StudentID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(50),
    Password VARCHAR(50),
    CNIC VARCHAR(20)
);

-- 3. Subject Table
CREATE TABLE Subject (
    SubjectID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(50),
    AcademicLevel VARCHAR(50)
);

-- 4. TutorSubject (Many-to-Many: Tutors and Subjects they teach)
CREATE TABLE TutorSubject (
    TutorID VARCHAR(50),
    SubjectID VARCHAR(50),
    PRIMARY KEY (TutorID, SubjectID),
    FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
    FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
);

-- 5. StudentSubject (Many-to-Many: Students and Subjects they want to learn)
CREATE TABLE StudentSubject (
    StudentID VARCHAR(50),
    SubjectID VARCHAR(50),
    PRIMARY KEY (StudentID, SubjectID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
);

-- 6. TutorStudent (Many-to-Many: Tutors and their Students)
CREATE TABLE TutorStudent (
    TutorID VARCHAR(50),
    StudentID VARCHAR(50),
    PRIMARY KEY (TutorID, StudentID),
    FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

-- 7. Session Table
CREATE TABLE Session (
    SessionID VARCHAR(50) PRIMARY KEY,
    DateTime DATETIME,
    Status VARCHAR(20),
    TutorID VARCHAR(50),
    StudentID VARCHAR(50),
    SubjectID VARCHAR(50),
    FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
);

-- 8. Feedback Table (Comments restricted to: 'Good', 'Bad', 'Ok')
CREATE TABLE Feedback (
    FeedbackID VARCHAR(50) PRIMARY KEY,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Comment VARCHAR(10) CHECK (Comment IN ('Good', 'Bad', 'Ok')),
    TutorID VARCHAR(50),
    StudentID VARCHAR(50),
    SessionID VARCHAR(50),
    FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (SessionID) REFERENCES Session(SessionID)
);
CREATE TABLE Education (
    EduID      INT IDENTITY(1,1) PRIMARY KEY,
    TutorID    VARCHAR(50),
    Education  VARCHAR(50),
    FOREIGN KEY (TutorID) REFERENCES Tutor(TutorID)
);
