-- >MySQL JOINS => used to combine rows from two or more tables based on a related column (usually a Primary Key and Foreign Key).
 -- 1):LEFT JOIN
 -- 2):RIGHT JOIN
 -- 3):INNER JOIN
 -- 4):FULL OUTER JOIN
 
    -- ? DEPARTMENT:
-- DEPT_ID       DEPT_NAME
-- 1             IT
-- 2             SOFTWARE
-- 3             HR
-- 4             FINANCE

    -- ? EMPLOYEE:
-- EMP_ID    EMP_NAME    DEPT_ID   
-- 100       ALICE       1
-- 101       RAHUL       3
-- 102       ATHUL       1
-- 103       BOB         2
-- 104       RAJU        
CREATE DATABASE JOINSS; 
USE JOINSS;
CREATE TABLE DEPARTMENT(DEPT_ID INT PRIMARY KEY,DEPT_NAME VARCHAR(50));
INSERT INTO DEPARTMENT VALUES(1,"IT"),(2,"SOFTWARE"),(3,"HR"),(4,"FINANCE");
SELECT * FROM DEPARTMENT;
CREATE TABLE EMPLOYEE(EMP_ID INT PRIMARY KEY,EMP_NAME VARCHAR(50),DEPT_ID INT,FOREIGN KEY(DEPT_ID)REFERENCES DEPARTMENT(DEPT_ID));
INSERT INTO EMPLOYEE VALUES(100,"ALICE",1),(101,"RAHUL",3),(102,"ATHUL",1),(103,"BOB",2),(104,"RAJU",NULL);
SELECT * FROM EMPLOYEE;

-- (1):LEFT JOIN => Returns all rows from the left table and the matching rows from the right table. If there is no match, the columns from the right table will contain NULL.
 -- SYNTAX:SELECT COLUMN_NAME FROM TABLE1  LEFT JOIN TABLE2 ON TABLE1.COLUMN_KEY=TABLE2.COLUMN_KEY;
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_NAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID; 

-- (2):RIGHT JOIN => Returns all rows from the right table and the matching rows from the left table. If there is no match in the left table, the left table's columns will contain NULL.
  -- SYNTAX:SELECT COLUMN_NAME FROM TABLE1  RIGHT JOIN TABLE2 ON TABLE1.COLUMN_KEY=TABLE2.COLUMN_KEY;
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_ID,D.DEPT_NAME FROM EMPLOYEE E RIGHT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID;

-- (3):INNER JOIN/JOIN => Returns only the rows that have matching values in both tables.
 -- SYNTAX:SELECT COLUMN_NAME FROM TABLE1  INNER JOIN TABLE2 ON TABLE1.COLUMN_KEY=TABLE2.COLUMN_KEY;
 SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_NAME FROM EMPLOYEE E INNER JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID;
 
-- (4):FULL OUTER => Returns:
--                      ✅ All rows from the left table
-- 					    ✅ All rows from the right table
--                      ✅ Matching rows are combined
--                      ✅ If there is no match, the missing columns are filled with NULL
-- LEFT JOIN UNION RIGHT JOIN
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_ID,D.DEPT_NAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID
UNION
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_ID,D.DEPT_NAME FROM EMPLOYEE E RIGHT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID;
 
 
-- 1. Display the employee ID, employee name, and department name for employees who are assigned to a valid department.
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_NAME FROM EMPLOYEE E INNER JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID;
-- 2. Display all employees along with their department names. Employees without a department should also be included.
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_NAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID;
-- 3.Display all departments along with the employees working in them. Departments with no employees should also be included.
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_NAME FROM EMPLOYEE E RIGHT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID;
-- 4. Display all employees and all departments, including:
-- employees without a matching department, and departments without any employees.
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_ID,D.DEPT_NAME FROM EMPLOYEE E LEFT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID
UNION
SELECT E.EMP_ID,E.EMP_NAME,D.DEPT_ID,D.DEPT_NAME FROM EMPLOYEE E RIGHT JOIN DEPARTMENT D ON E.DEPT_ID=D.DEPT_ID;
 



-- >DATE FUNCTIONS
 -- 1)CURDATE() => RETURNS CURRENT DATE (YYYY-MM-DD)
SELECT CURDATE();
 
 -- 2)CURRENTDATE() => RETURNS CURRENT DATE (YYYY-MM-DD)
 SELECT CURRENT_DATE();
 
 -- 3)NOW() => RETURNS CURRENT DATE AND TIME
SELECT NOW() AS "DATE N TIME";
 
 -- 4)CURTIME() => REURNS CURRENT TIME
 SELECT CURTIME();
 
 -- 5)YEAR() => EXTRACTS THE YEAR
 SELECT YEAR("2026-08-07");
	  -- OR
 SELECT YEAR(NOW());   
 
 -- 6)MONTH() => EXTRACTS THE MONTH
 SELECT MONTH("2026-08-07");
      -- OR
 SELECT MONTH(NOW());
 
 -- 7)MONTHNAME() => RETURNS MONTH NAME
 SELECT MONTHNAME("2026-08-07");
       -- OR
 SELECT MONTHNAME(NOW());
 
 -- 8)DAY() => RETURNS DAY OF THE MONTH
 SELECT DAY("2026-08-07");
       -- OR
 SELECT DAY(NOW());
 
 -- 9)DAYNAME() => RETURNS THE WEEKDAY NAME
 SELECT DAYNAME("2026-08-07");
       -- OR
 SELECT DAYNAME(NOW());
 
 -- 10)DAYOFWEEK() => RETURNS WEEKDAY NUMBER
  SELECT DAYOFWEEK("2026-08-07");
       -- OR
 SELECT DAYOFWEEK(NOW());
 
 -- 11)DAYOFYEAR() => RETURNS DAY NUMBER IN THE YEAR
  SELECT DAYOFYEAR("2026-08-07");
       -- OR
 SELECT DAYOFYEAR(NOW());
 
 -- 12)WEEK() => RETURNS WEEK NUMBER
  SELECT WEEK("2026-08-07");
       -- OR
 SELECT WEEK(NOW());
 
 -- 13)QUARTER() => RETURNS QUARTER NUMBER
  SELECT QUARTER("2026-08-07");
       -- OR
 SELECT QUARTER(NOW());
 
 -- 14)HOUR() => EXTRACTS HOUR
 SELECT HOUR(CURTIME());
 
 -- 15)MINUTE() => EXTRACTS MINUTES
 SELECT MINUTE(CURTIME());
 
 -- 16)SECOND() => EXTRACTS SECONDS
 SELECT SECOND(NOW());
 


-- DATE ARITHMETIC FUNCTIONS
 -- 1)DATE_ADD() => ADDS A SPECIFIED INTERVAL TO A  DATE
SELECT DATE_ADD("2026-08-15",INTERVAL 10 DAY) AS "NEW DATE";
 -- MONTH,YEAR,WEEK,HOUR,MINUTE,SECOND
 
 -- 2)DATE_SUB() => SUBTRACTS A SPECIFIED INTERVAL FROM A DATE
SELECT DATE_SUB(NOW(),INTERVAL 2 MONTH);
 
 -- 3)DATEDIFF() => RETURNS NUMBER OF DAYS BETWEEEN TWO DATES
SELECT DATEDIFF(NOW(),"2025-01-01");
 
	 -- DATE FORMATTING --
--  FORMAT        MEANING
 --  %d           day(01-31)
 --  %m           month(01-12)
 --  %Y           4 DIGIT YEAR
 --  %y           2 digit YEAR
 --  %M           FULL MONTH NAME
 --  %b           short month name
 --  %W           FULL WEEK NAME
 --  %a           short week name
 SELECT DATE_FORMAT("2026-08-07","%d-%m-%y") AS DATE;
-- ?FRIDAY-AUGUST 7-2026
SELECT DATE_FORMAT(NOW(),"%W-%M %d-%Y") AS DATE;
-- ?FRIDAY, AUG 07, 26
SELECT DATE_FORMAT(NOW(),"%W,%M %d,%y") AS DATE;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 