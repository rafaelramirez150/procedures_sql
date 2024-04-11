CREATE DATABASE EMP;
USE EMP;
CREATE TABLE employees (
EMPLOYEE_ID int DEFAULT NULL,
FIRST_NAME text,
LAST_NAME text,
EMAIL text,
PHONE_NUMBER text,
HIRE_DATE datetime DEFAULT NULL,
JOB_ID text,
SALARY int DEFAULT NULL,
COMISSION_PCT text,
MANAGER_ID text DEFAULT NULL,
DEPRTAMENT_ID int DEFAULT NULL
)ENGINE InnoDB;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/employees.csv'
into table employees
fields terminated by "|"
enclosed by	","
lines terminated by "\r\n"
ignore 1 lines;

select * from eemployees;

select @@global.secure_file_priv;

drop database emp;

show variables like 'secure_file_priv';