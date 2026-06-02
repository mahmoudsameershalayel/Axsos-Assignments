# Counter App

A Django app that tracks page visits and a manually controlled counter using sessions.

## Features

- Displays how many times the user has visited the page
- Displays the current counter value (separate from visit count)
- **+2 button** — increments the counter by 2
- **Custom increment form** — enter any number to increment the counter by that amount
- **Reset button** — clears both the visit count and counter value

## Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Home page; increments visit count |
| `/increment_by_two` | GET | Increments counter by 2 |
| `/increment_by_amount` | POST | Increments counter by a user-specified amount |
| `/destroy_session` | GET | Resets counter and visit count |

## Setup

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/`.
