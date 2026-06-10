# Books & Authors

A Django app demonstrating a many-to-many relationship between books and authors.

## Models

- **Book** — title, description
- **Author** — first name, last name, notes
- An author can have many books; a book can have many authors.

## Features

- View all books / authors
- Add a new book or author
- View a book's detail page with its associated authors
- View an author's detail page with their associated books
- Add an author to a book (dropdown shows only unassociated authors)
- Add a book to an author (dropdown shows only unassociated books)

## Setup

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/books/` or `http://127.0.0.1:8000/authors/`.
