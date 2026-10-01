CREATE DATABASE WORK2;
USE WORK2;
SHOW TABLES;
CREATE TABLE DEPARTMENTS(DEPT_ID INT PRIMARY KEY ,DEPT_NAME VARCHAR(50));
INSERT INTO DEPARTMENTS VALUES(1,"HR"),(2,"FINANCE");
CREATE TABLE EMPLOYEES(EMP_ID INT PRIMARY KEY,EMP_NAME VARCHAR(50),EMP_SALARY DEC(10,2),DEPT_ID INT,FOREIGN KEY(DEPT_ID) REFERENCES DEPARTMENTS(DEPT_ID));
INSERT INTO EMPLOYEES VALUES(1,"John Smith",50000,1),(2,"Jane Doe",60000,2),(3,"Michael Lee",55000,1);
SELECT * FROM EMPLOYEES;
SELECT * FROM DEPARTMENTS;
-- 1)Retrieve all employee names and their corresponding department names. 
SELECT E.EMP_NAME,D.DEPT_NAME FROM EMPLOYEES E JOIN DEPARTMENTS D ON E.EMP_ID=D.DEPT_ID;

-- 2) Find the total salary for each department. 
SELECT DEPT_ID,SUM(EMP_SALARY) AS TOTAL_SALARY FROM EMPLOYEES GROUP BY DEPT_ID;

-- 3) Get the highest salary among all employees. 
SELECT MAX(EMP_SALARY) AS HIGHEST_SALARY FROM EMPLOYEES;

-- 4) List employees who have a salary greater than 55000 and belong to the 'HR' department. 
SELECT E.EMP_NAME,EMP_SALARY FROM EMPLOYEES E JOIN DEPARTMENTS D ON E.DEPT_ID=D.DEPT_ID WHERE E.EMP_SALARY>55000 AND D.DEPT_NAME="HR";

-- 5) Update the salary of employee with id 2 to 65000. 
UPDATE  EMPLOYEES SET EMP_SALARY=65000 WHERE EMP_ID=2;
SELECT * FROM EMPLOYEES;

-- 6)Count the number of employees in each department. 
SELECT DEPT_ID,COUNT(*) AS EMPLOYEE_COUNT FROM EMPLOYEES GROUP BY DEPT_ID;

-- 7) Find the average salary of employees in each department. 
SELECT DEPT_ID,AVG(EMP_SALARY) AS AVG_SALARY FROM EMPLOYEES GROUP BY DEPT_ID;

-- 8) List the employees with their names and salaries in descending order of salary.
SELECT EMP_NAME,EMP_SALARY FROM EMPLOYEES ORDER BY EMP_SALARY DESC;

 -- 9) Retrieve the department names and the number of employees in each department, including departments with no employees. 
 SELECT D.DEPT_NAME, COUNT(*) AS EMPLOYEE_COUNT FROM DEPARTMENTS D LEFT JOIN EMPLOYEES E ON D.DEPT_ID=E.DEPT_ID GROUP BY D.DEPT_NAME;
 
--  10) Find the total number of employees and the total sum of salaries for the entire organization.
SELECT COUNT(*) AS TOTAL_EMPLOYEES,SUM(EMP_SALARY) AS TOTAL_SALARY FROM EMPLOYEES;

--  11) Increase the salary of all employees in the 'HR' department by 10%. 
UPDATE EMPLOYEES SET EMP_SALARY=EMP_SALARY*1.10 WHERE DEPT_ID=(SELECT DEPT_ID FROM DEPARTMENTS WHERE DEPT_NAME="HR");

--  12) Find the department names where the average salary is higher than the average salary of the entire organization.
SELECT D.DEPT_NAME,AVG(E.EMP_SALARY)AS AVG_SALARY FROM EMPLOYEES E JOIN DEPARTMENTS D ON E.DEPT_ID=D.DEPT_ID 
GROUP BY D.DEPT_NAME HAVING AVG(E.EMP_SALARY)>(SELECT AVG(EMP_SALARY) FROM EMPLOYEES);

--  13) List the employee names who earn more than the highest salary in the 'Finance' department.
SELECT EMP_NAME FROM EMPLOYEES WHERE EMP_SALARY>(SELECT MAX(E.EMP_SALARY)FROM EMPLOYEES E JOIN DEPARTMENTS D ON E.DEPT_ID=D.DEPT_ID WHERE D.DEPT_NAME="FINANCE");

--  14) Retrieve the employee names who earn more than the lowest salary in the organization but less than the highest salary in the 'HR' department. 
SELECT EMP_NAME, EMP_SALARY
FROM EMPLOYEES
WHERE EMP_SALARY > (
    SELECT MIN(EMP_SALARY)
    FROM EMPLOYEES)
AND EMP_SALARY < (
    SELECT MAX(E.EMP_SALARY)
    FROM EMPLOYEES E
    JOIN DEPARTMENTS D
    ON E.DEPT_ID = D.DEPT_ID
    WHERE D.DEPT_NAME = 'HR'
);