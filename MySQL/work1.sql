-- CREATE A TABLE FOR STUDENT DETAILS WITH THE FOLLOWING COLUMNS:
-- * student id
-- * name
-- * age
-- * gender
-- * course name
-- * city
-- * marks
-- * fees
CREATE DATABASE WORK1;
USE WORK1;
CREATE TABLE STUDENT(ID INT,NAME VARCHAR(50),AGE INT,GENDER VARCHAR(50),COURSE VARCHAR(50),CITY VARCHAR(50),MARKS INT ,FEES INT);
INSERT INTO STUDENT VALUES(1,"ADHIL",21,"MALE","PYTHON","CALICUT",98,50000),
                          (2,"MISHAL",22,"MALE","FLUTTER","MALAPPURAM",90,60000),
                          (3,"ANSHIN",20,"MALE","PYTHON","KOCHI",93,50000),
						  (4,"RISHAL",25,"MALE","DATASCIENCE","CALICUT",88,75000),
                          (5,"DILSHA",28,"FEMALE","FULLSTACK","MALAPPURAM",78,60000),
                          (6,"DILIN",29,"MALE","PYTHON","CALICUT",98,50000),
						  (7,"SALINI",25,"FEMALE","DATASCIENCE","CALICUT",95,75000),
                          (8,"AMMU",21,"FEMALE","FULLSTACK","CALICUT",97,60000);
-- Insert 8 records.
-- #### **Questions**
-- 1. Display all the records from the students table.
-- 2. Display only the student name, course, and marks.
-- 3. Rename the column fees as course\_fees.
-- 4. Display the details of students who scored more than 80 marks.
-- 5. Display the details of students whose marks are between 60 and 80.
-- 6. Display the details of students who belong to Kochi or Calicut.
-- 7. Increase the fees by ₹2,000 for all students enrolled in the Data Science course.
-- 8. Remove the records of students who scored less than 35 marks.
-- 9. Display the details of the top five students based on their marks.
-- 10. Display all students by arranging them first according to their marks in descending order and then by age in ascending order.
-- 11. Display the list of cities without repeating any city name.
-- 12. Display each student's name along with their marks after adding a bonus of 10 marks.
-- 13. Display the highest mark, lowest mark, average mark, total fees collected, and total number of students.
-- 14. Display the number of students enrolled in each course.
-- 15. Display the courses that have more than three students enrolled.
-- 16. Display a report containing the student's name, course, marks, and fees after applying a 5% discount.
-- 17. Display the names of students whose names start with the letter A.
-- 18. Display the city that has the highest number of students.
-- 19. Remove the column gender from the table.
-- 20. Display the number of students in each course and show only courses having more than 3 students.
SELECT * FROM STUDENT;
SELECT NAME,COURSE,MARKS FROM STUDENT;
ALTER TABLE STUDENT RENAME COLUMN FEES TO COURSE_FEES;
SELECT * FROM STUDENT WHERE MARKS>80;
SELECT * FROM STUDENT WHERE MARKS BETWEEN 60 AND 80;
SELECT * FROM STUDENT WHERE CITY IN ("KOCHI","CALICUT");
UPDATE STUDENT SET COURSE_FEES=COURSE_FEES+2000 WHERE COURSE="DATASCIENCE";
DELETE FROM STUDENT WHERE MARKS<35;
SELECT * FROM STUDENT ORDER BY MARKS DESC LIMIT 5;
SELECT * FROM STUDENT ORDER BY MARKS DESC,AGE ASC;
SELECT DISTINCT CITY FROM STUDENT;
SELECT NAME,MARKS,MARKS+10 AS BONUS_MARKS FROM STUDENT;
SELECT MAX(MARKS) AS HIGHEST_MARK,MIN(MARKS) AS LOWEST_MARK,AVG(MARKS) AS AVERAGE_MARK,SUM(COURSE_FEES) AS TOTAL_FEES,COUNT(*) AS TOTAL_STUDENTS FROM STUDENT;
SELECT COURSE,COUNT(*) AS TOTAL_STUDENTS FROM STUDENT GROUP BY COURSE;
SELECT COURSE,COUNT(*) AS TOTAL_STUDENTS FROM STUDENT GROUP BY COURSE HAVING COUNT(*)>3;
SELECT NAME,COURSE,MARKS,COURSE_FEES;
SELECT NAME FROM STUDENT WHERE NAME LIKE "A%";
SELECT CITY,COUNT(*) AS TOTAL_STUDENTS FROM STUDENT GROUP BY CITY ORDER BY TOTAL_STUDENTS DESC LIMIT 1;
ALTER TABLE STUDENT DROP COLUMN GENDER; 
SELECT COURSE,COUNT(*) AS TOTAL_STUDENTS FROM STUDENT GROUP BY COURSE HAVING COUNT(*)>3;