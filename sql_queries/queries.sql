-- CREATE TABLE users(
-- user_id INT PRIMARY KEY,
-- user_name VARCHAR(50),
-- email VARCHAR(50)
-- );

CREATE TABLE tasks(
task_id INT PRIMARY KEY,
tag_id INT,
project_id INT,
task_name VARCHAR(50),
status VARCHAR(50),
due_date TIMESTAMP,
constraint task_user_fk foreign key (project_id)
references project (project_id),
constraint task_tag_fk foreign key (tag_id)
references tags(tag_id)

);
drop table tasks;
CREATE TABLE tags (
tag_id INT PRIMARY KEY,
tag_name VARCHAR(50)
);
CREATE TABLE project (
project_id INT PRIMARY KEY,
projectname VARCHAR(50),
user_id INT,
CONSTRAINT project_user_fk foreign key (user_id)
references users (user_id)
);
-- drop table project;
INSERT INTO users(user_id, user_name, email)
VALUES(
3, 'charlie', 'charlie@email.com '
);
INSERT INTO tasks(task_id, task_name, project_id, status, due_date, tags )
VALUES (
6, 'renew passport', 4, 'pending', '2025-09-05', 5
)
INSERT INTO tags(tag_id, tag_name)
VALUES (
5, 'travel'
)
INSERT INTO project (project_id, projectname, user_id)
VALUES (
4, 'travel plans', 3
)