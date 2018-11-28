drop table department;
create table if not exists department (id integer primary key, name varchar(40));

drop table employee;
create table if not exists employee (id integer primary key, department_id integer, chief_doc_id integer, name varchar(40), num_public integer, foreign key (department_id) references department (id));

insert into department values
('1', 'Therapy'), ('2', 'Neurology'), ('3', 'Cardiology'), ('4', 'Gastroenterology'), ('5', 'Hematology'), ('6', 'Oncology');

insert into employee values
('1', '1', '1', 'Kate', 4), ('2', '1', '1', 'Lidia', 2), ('3', '1', '1', 'Alexey', 1), ('4', '1', '2', 'Pier', 7), ('5', '1', '2', 'Aurel', 6),
('6', '1', '2', 'Klaudia', 1), ('7', '2', '3', 'Klaus', 12), ('8', '2', '3', 'Maria', 11), ('9', '2', '4', 'Kate', 10), ('10', '3', '5', 'Peter', 8),
('11', '3', '5', 'Sergey', 9), ('12', '3', '6', 'Olga', 12), ('13', '3', '6', 'Maria', 14), ('14', '4', '7', 'Irina', 2), ('15', '4', '7', 'Grit', 10), ('16', '4', '7', 'Vanessa', 16), ('17', '5', '8', 'Sascha', 21), ('18', '5', '8', 'Ben', 22), ('19', '6', '9', 'Jessy', 19), ('20', '6', '9', 'Ann', 18);

--запрос 1 выводит подсчет количества главных врачей в каждом департементе
select name, count(id_tmp) as chief_docs from (
select id_tmp, name from 
(select id_tmp, department_id from ( 
select distinct chief_doc_id as id_tmp from employee) as tmp1
inner join
employee
on tmp1.id_tmp=employee.id) as tmp2
inner join department
on department.id=tmp2.department_id) as tmp3
group by name;

--запрос 2
select count(id), department_id from employee group by department_id having count(id) > 2;

--запрос 3 (максимальное определяется путем сравнения со средним значением)

select department_id, count(num_public) as num from employee 
group by department_id 
having count(num_public)>(select avg(num) from (
select department_id, count(num_public) as num from employee group by department_id order by num desc) as tmp2)
order by num desc;

--запрос 4
select name1 as name_dep, name_emp, num_public from
(select name as name1, name_emp, department_id, num_public, row_number() over (partition by department_id order by num_public asc) as num
from department 
full join 
(select department_id, name as name_emp, num_public from employee) as tmp2 
on department.id=tmp2.department_id) tmp5

full join

(select name as name2, avg(num_public) as avg from department 
full join 
(select department_id, name as name_emp, num_public from employee) as tmp3 
on department.id=tmp3.department_id
group by name) as tmp4
on tmp5.name1=tmp4.name2
where num_public<avg;


--запрос 5
select name, round(avg,2) from (
select name, count(id_tmp) as chief_docs from (
select id_tmp, name from 
(select id_tmp, department_id from ( 
select distinct chief_doc_id as id_tmp from employee) as tmp1
inner join
employee
on tmp1.id_tmp=employee.id) as tmp2
inner join department
on department.id=tmp2.department_id) as tmp3
group by name
having count(id_tmp)>1) as tmp6

inner join

(select department_id, name, avg from (
select department_id, avg(num_public) from employee group by department_id) as tmp4
inner join
department
on department.id=tmp4.department_id) as tmp5
using(name);

