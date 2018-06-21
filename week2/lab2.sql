CREATE TABLE INSTRUCTOR
  (ins_id INTEGER PRIMARY KEY NOT NULL, 
   lastname VARCHAR(15) NOT NULL, 
   firstname VARCHAR(15) NOT NULL, 
   city VARCHAR(15), 
   country CHAR(2)
  );
------------------------------------------
--DDL statement for table 'HR' database--
--------------------------------------------

CREATE TABLE EMPLOYEES (
                            EMP_ID CHAR(9) NOT NULL, 
                            F_NAME VARCHAR(15) NOT NULL,
                            L_NAME VARCHAR(15) NOT NULL,
                            SSN CHAR(9),
                            B_DATE DATE,
                            SEX CHAR,
                            ADDRESS VARCHAR(30),
                            JOB_ID CHAR(9),
                            SALARY DECIMAL(10,2),
                            MANAGER_ID CHAR(9),
                            DEP_ID CHAR(9) NOT NULL,
                            PRIMARY KEY (EMP_ID));
                            
  CREATE TABLE JOB_HISTORY (
                            EMPL_ID CHAR(9) NOT NULL, 
                            START_DATE DATE,
                            JOBS_ID CHAR(9) NOT NULL,
                            DEPT_ID CHAR(9),
                            PRIMARY KEY (EMPL_ID,JOBS_ID));
 
 CREATE TABLE JOBS (
                            JOB_IDENT CHAR(9) NOT NULL, 
                            JOB_TITLE VARCHAR(15) ,
                            MIN_SALARY DECIMAL(10,2),
                            MAX_SALARY DECIMAL(10,2),
                            PRIMARY KEY (JOB_IDENT));

CREATE TABLE DEPARTMENTS (
                            DEPT_ID_DEP CHAR(9) NOT NULL, 
                            DEP_NAME VARCHAR(15) ,
                            MANAGER_ID CHAR(9),
                            LOC_ID CHAR(9),
                            PRIMARY KEY (DEPT_ID_DEP));

CREATE TABLE LOCATIONS (
                            LOCT_ID CHAR(9) NOT NULL,
                            DEP_ID_LOC CHAR(9) NOT NULL,
                            PRIMARY KEY (LOCT_ID,DEP_ID_LOC));
                            

INSERT INTO INSTRUCTOR
  (ins_id, lastname, firstname, city, country)
  VALUES 
  (1, 'Ahuja', 'Rav', 'Toronto', 'CA')
;

INSERT INTO INSTRUCTOR
  VALUES
  (2, 'Chong', 'Raul', 'Toronto', 'CA'),
  (3, 'Vasudevan', 'Hima', 'Chicago', 'US')
;

SELECT * FROM INSTRUCTOR
;

SELECT firstname, lastname, country from INSTRUCTOR where city='Toronto'
;

UPDATE INSTRUCTOR SET city='Markham' where ins_id=1
;

DELETE FROM INSTRUCTOR where ins_id=2
;

SELECT * FROM INSTRUCTOR 
;

------------------------------------------
--Load values from .csv files for Employees, Departments, Jobs, Locations, JobsHistory using IBM DB2--
--------------------------------------------

--Query 1: Retreive all employees whose address is in Elgin,IL--
SELECT F_NAME, L_NAME FROM Employees
   WHERE ADDRESS LIKE '%Elgin,IL';

--Query 2: Retrieve all employees who were born during the 1970's--   
SELECT F_NAME, L_NAME FROM Employees
  WHERE B_DATE LIKE '%197%';

--Query 3: Retrieve all employees in department 5 whose salary is between 60000 and 70000--
SELECT * FROM EMPLOYEES 
  WHERE (SALARY BETWEEN 60000 AND 70000) AND DEP_ID=5;
  
--Query 4: Retrieve a list of employees ordered by department name, and within each department ordered-- 
--alphabetically in descending order by last name--
SELECT D.DEP_NAME, E.F_NAME, E.L_NAME
FROM DEPARTMENTS AS D, EMPLOYEES AS E
WHERE E.DEP_ID = D.DEPT_ID_DEP
ORDER BY D.DEP_NAME, E.L_NAME DESC ;

--Query 5: Retrieve the department number, the number of employees in the department, and the avg salary--
SELECT DEP_ID, COUNT(*), AVG(SALARY)
FROM EMPLOYEES
GROUP BY DEP_ID;
  

