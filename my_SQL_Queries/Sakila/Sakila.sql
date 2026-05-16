/*1. What query would you run to get all the customers inside city_id = 312? Your query should return the customer's first name, last name, email, and address.*/
use sakila;
select c.first_name, c.last_name, c.email, a.address
from customer c
join address a
on c.address_id = a.address_id
where a.city_id = 312;

/* 2. What query would you run to get all comedy films? Your query should return the film title, description, release year, rating, special features, and genre (category). */
select f.title, f.description, f.release_year, f.rating,f.special_features, c.name
from film f
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id 
where c.name = 'comedy';

/* 3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor ID, name, film title, description, and release year. */
select a.actor_id, concat(a.first_name , ' ' , a.last_name) name, f.title, f.description, f.release_year
from actor a
join film_actor fa on fa.actor_id = a.actor_id
join film f on f.film_id = fa.film_id
where a.actor_id = 5;

/* 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312, and 459)? Your query should return the customer's first name, last name, email, and address. */
select c.first_name, c.last_name, c.email, a.address
from customer c 
join address a on c.address_id = a.address_id
where c.store_id = 1 AND a.city_id in (1, 42, 312, 459);

/* 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use the LIKE function to get the 'behind the scenes' part. */
select f.title, f.description, f.release_year, f.rating,f.special_features
from actor a
join film_actor fa on fa.actor_id = a.actor_id
join film f on f.film_id = fa.film_id
where a.actor_id = 15 AND f.rating = 'G' AND f.special_features LIKE '%Behind the Scenes%';

/* 6. What query would you run to get all the actors joining the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name. */
select f.film_id, f.title, a.actor_id, concat(a.first_name , ' ' , a.last_name) actor_name
from actor a
join film_actor fa on fa.actor_id = a.actor_id
join film f on f.film_id = fa.film_id
where f.film_id = 369;

/* 7. What query would you run to get all drama films with a rental rate of 2.99? Your query should return the film title, description, release year, rating, special features, and genre (category). */
select f.title, f.description, f.release_year, f.rating,f.special_features, c.name
from film f
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id 
where c.name = 'Drama' AND f.rental_rate = 2.99;

/* 8. What query would you run to get all the action films joined by SANDRA KILMER? Your query should return the film title, description, release year, rating, special features, genre (category), and actor's first and last name. */
select f.title, f.description, f.release_year, f.rating, f.special_features, c.name, concat(a.first_name, ' ', a.last_name) actor_name
from actor a
join film_actor fa on a.actor_id = fa.actor_id
join film f on fa.film_id = f.film_id
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id
where a.first_name = 'SANDRA'
AND a.last_name = 'KILMER'
AND c.name = 'Action';
