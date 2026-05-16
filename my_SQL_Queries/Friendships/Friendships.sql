-- create database Friendships;
use Friendships;
-- Forward engineer the friendships_schema from the previous chapter
/*create table users(
	id int auto_increment primary key,
    first_name varchar(100),
    last_name varchar(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table friendships(
	id int auto_increment primary key,
	user_id INT,
    friend_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
)*/

-- Query: Create 6 new users
/*
INSERT INTO users (first_name, last_name)
VALUES 
('Amy', 'Giver'),
('Eli', 'Byers'),
('Marky', 'Mark'),
('Big', 'Bird'),
('Kermit', 'The Frog'),
('John', 'Doe');
*/
-- Query: Have user 1 be friends with users 2, 4, and 6
/*
insert into friendships(user_id, friend_id)
values
(1,2),
(1,4),
(1,6)
*/
-- Query: Have user 2 be friends with users 1, 3, and 5
/*
insert into friendships(user_id, friend_id)
values
(2,1),
(2,3),
(2,5)
*/

-- Query: Have user 3 be friends with users 2 and 5
/*
insert into friendships(user_id, friend_id)
values
(3,2),
(3,5)
*/

-- Query: Have user 4 be friends with user 3
/*
insert into friendships(user_id, friend_id)
values
(4,3)
*/

-- Query: Have user 5 be friends with users 1 and 6
/*
insert into friendships(user_id, friend_id)
values
(5,1),
(5,6)
*/
-- Query: Have user 6 be friends with users 2 and 3
/*
insert into friendships(user_id, friend_id)
values
(6,2),
(6,3)
*/

-- Query: Display the relationships created as shown in the above image
select u.first_name, u.last_name, u2.first_name friend_first_name, u2.last_name friend_last_name
from users u
join friendships f on u.id = f.user_id
join users u2 on f.friend_id = u2.id;

-- NINJA Query: Return all users who are friends with the first user, and make sure their names are displayed in the results.
SELECT u2.first_name, u2.last_name
FROM friendships f
JOIN users u2 ON f.friend_id = u2.id
WHERE f.user_id = 1;


-- NINJA Query: Return the count of all friendships
select count(*)
from friendships;

-- NINJA Query: Find out who has the most friends and return the count of their friends.
select concat(u.first_name, ' ', u.last_name)full_name, count(*) total_friends
from users u
join friendships f on f.user_id = u.id
group by u.id 
order by total_friends desc
LIMIT 1;

-- NINJA Query: Return the friends of the third user in alphabetical order
select u.first_name, u.last_name, u2.first_name friend_first_name, u2.last_name friend_last_name
from users u
join friendships f on f.user_id = u.id
join users u2 on f.friend_id = u2.id
where u.id = 3
order by u2.first_name ASC


