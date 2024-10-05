-- command to initialize it:
-- sqlite3 zetechsystem.db < ZetechAssg1.sql


-- creating database
-- CREATE DATABASE ZETECHSYSTEM;


-- -- creating table
-- USE ZETECHSYSTEM;

-- Creating the table
CREATE TABLE STUDENTS_DETAILS (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Address TEXT
);

-- Inserting records into the STUDENTS_DETAILS table
INSERT INTO STUDENTS_DETAILS (StudentID, StudentName, Age, Address) VALUES
(1400, 'Ann Maina', 18, 'Nairobi'),
(1401, 'Jane Onyango', 21, 'Kisumu'),
(1402, 'Jack Ombote', 22, 'Swaziland'),
(1403, 'Susan Mutiso', 20, 'Kitui'),
(1404, 'Erick Mwema', 17, 'Machakos'),
(1405, 'Janet Kirigo', 19, 'Swaziland'),
(1406, 'Erick Mwema', 17, 'Nyamira');

-- View the records
SELECT * FROM STUDENTS_DETAILS;

-- Update Ann Maina's address to Mandera
UPDATE STUDENTS_DETAILS
SET Address = 'Mandera'
WHERE StudentName = 'Ann Maina';

-- Arrange the records by Address in ascending order
SELECT * FROM STUDENTS_DETAILS
ORDER BY Address;

-- Delete Susan Mutiso's record
DELETE FROM STUDENTS_DETAILS
WHERE StudentName = 'Susan Mutiso';

-- Extract names of students residing in Swaziland
SELECT StudentName FROM STUDENTS_DETAILS
WHERE Address = 'Swaziland';

-- Display students' names starting with the letter 'J'
SELECT StudentName FROM STUDENTS_DETAILS
WHERE StudentName LIKE 'J%';

-- Display all records of students named Erick Mwema aged 17
SELECT * FROM STUDENTS_DETAILS
WHERE StudentName = 'Erick Mwema' AND Age = 17;