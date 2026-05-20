# First Django Project

This is a simple Django intro project with one app named `first_app`.

The app currently contains placeholder blog routes for practicing Django URL routing,
views, redirects, and JSON responses.

## Project Structure

```text
first_project/
|-- manage.py
|-- db.sqlite3
|-- first_project/
|   |-- settings.py
|   `-- urls.py
`-- first_app/
    |-- urls.py
    |-- views.py
    |-- models.py
    `-- tests.py
```

## How to Run

From the project folder, run:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## App Routes

| URL | Description |
| --- | --- |
| `/` | Redirects to `/blogs` |
| `/blogs` | Placeholder for all blogs |
| `/blogs/new` | Placeholder for a new blog form |
| `/blogs/create` | Redirects back to `/` |
| `/blogs/<number>` | Placeholder for showing one blog |
| `/blogs/<number>/edit` | Placeholder for editing one blog |
| `/blog/json` | Intended route for returning blog data as JSON |

## Notes

This project is for learning Django basics. The views currently return simple
placeholder responses and can be expanded later with templates, models, and forms.
