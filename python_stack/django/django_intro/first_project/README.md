# First Django Project

A multi-app Django project practicing URL routing, views, and redirects across three independent apps.

## Project Structure

```
first_project/
├── manage.py
├── first_project/       # project config
│   ├── settings.py
│   └── urls.py
├── first_app/           # blogs app
│   ├── urls.py
│   └── views.py
├── surveys_app/         # surveys app
│   ├── urls.py
│   └── views.py
└── users_app/           # users app
    ├── urls.py
    └── views.py
```

## Setup

Activate the virtual environment, then run:

```bash
py manage.py runserver
```

## Routes

### Blogs (`first_app`)

| URL | Method | Description |
|-----|--------|-------------|
| `/` | `index` | Same as `/blogs` (ninja bonus) |
| `/blogs/` | `index` | List all blogs |
| `/blogs/new` | `new` | New blog form |
| `/blogs/create` | `create` | Redirects to `/blogs` |
| `/blogs/<number>` | `show` | Show one blog |
| `/blogs/<number>/edit` | `edit` | Edit one blog |
| `/blogs/<number>/delete` | `destroy` | Redirects to `/blogs` |

### Surveys (`surveys_app`)

| URL | Method | Description |
|-----|--------|-------------|
| `/surveys/` | `index` | List all surveys |
| `/surveys/new` | `new` | New survey form |

### Users (`users_app`)

| URL | Method | Description |
|-----|--------|-------------|
| `/register` | `register` | Register a new user |
| `/users/new` | `register` | Same as `/register` |
| `/login` | `user_login` | Log in |
| `/users` | `index` | List all users |
