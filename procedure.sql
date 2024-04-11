delimiter $$
create procedure ns
(fi date, ff date)

begin
SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN %s AND %s

end$$

delimiter;
