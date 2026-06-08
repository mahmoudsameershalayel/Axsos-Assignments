# Shell Dojo Ninjas

A Django app for managing dojos and their associated ninjas.

## Features

- Add dojos (name, city, state)
- Add ninjas and assign them to a dojo
- View all dojos with their ninja rosters and ninja count
- Delete a dojo (cascades to all its ninjas)

## Setup

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Models

- **Dojo** — name, city, state
- **Ninja** — first name, last name, foreign key to Dojo
