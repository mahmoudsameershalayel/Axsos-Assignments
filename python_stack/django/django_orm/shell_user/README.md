# Shell User - Django ORM Practice

A Django project for practicing ORM queries and building a basic user management interface.

## Features

- `User` model with first name, last name, email, and age fields
- List all users on the home page
- Create new users via a form
- Django shell ORM query practice (see `queries.txt`)

## Setup

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

## Project Structure

```
shell_user/
├── shell_app/
│   ├── models.py       # User model
│   ├── views.py        # index and create_user views
│   ├── urls.py         # app-level URL patterns
│   └── templates/
│       └── index.html
├── shell_user/
│   ├── settings.py
│   └── urls.py
├── queries.txt         # Django shell ORM query examples
└── manage.py
```

## ORM Examples

See [queries.txt](queries.txt) for shell examples covering:

- `User.objects.create()`
- `User.objects.all()`, `.first()`, `.last()`
- `User.objects.get(id=...)`
- Updating and saving a record
- Deleting a record
- Ordering with `.order_by()`
