create database team_data;
use team_data;
create table users(
id int primary key,
name varchar(100),
age int,
cgpa float
);
insert into users (name, id, age, cgpa)
values ('Hana Amro Sayed', 22011603, 20, 3.8651),
('Maya Bastawy Ahmed', 22011511, 20, 3.5777),
('Tibyan Ashraf Abdullah', 22011497, 19, 3.7331),
('Shahd Medhat Tawfeek', 22010354, 20, 3.9435),
('Yasmine Ali Abdelrahman', 22010292, 19, 4.000);
select * from team_data.users;