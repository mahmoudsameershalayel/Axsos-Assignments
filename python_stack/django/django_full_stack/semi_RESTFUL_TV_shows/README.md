# Semi-RESTful TV Shows

A Django web app for managing a list of TV shows with full CRUD functionality.

## Features

- View all TV shows
- Add a new show
- Edit an existing show
- Delete a show
- Server-side validation (title uniqueness, release date, field lengths)

## Setup

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/`

## Routes

| Method | URL | Action |
|--------|-----|--------|
| GET | `/shows/` | List all shows |
| GET | `/shows/new/` | New show form |
| POST | `/shows/create/` | Create a show |
| GET | `/shows/<id>/` | Show details |
| GET | `/shows/<id>/edit/` | Edit show form |
| POST | `/shows/<id>/update/` | Update a show |
| POST | `/shows/<id>/destroy/` | Delete a show |

## Validations

- Title: required, min 2 characters, must be unique
- Network: required, min 3 characters
- Release date: required, must not be in the future
- Description: optional, min 10 characters if provided
