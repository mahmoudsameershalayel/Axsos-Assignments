semi_RESTFUL_TV_shows_app

Simple Django app for the "Semi RESTful TV Shows" assignment.

Overview
- This app manages TV shows with views to list, create, edit, and show details.
- Templates live in `semi_RESTFUL_TV_shows_app/templates/` and static files in `semi_RESTFUL_TV_shows_app/static/`.

Quick start
1. From the project root, ensure dependencies are installed (Python, Django).
2. Run the development server:

   python manage.py runserver

3. Open http://127.0.0.1:8000/ and navigate to the app routes (see project URLs).

Notes
- Database migrations are stored in `semi_RESTFUL_TV_shows_app/migrations/`.
- To reset the DB during development, delete `db.sqlite3` and run `python manage.py migrate`.

Files of interest
- `semi_RESTFUL_TV_shows_app/views.py` — request handlers
- `semi_RESTFUL_TV_shows_app/urls.py` — app URL patterns
- `semi_RESTFUL_TV_shows_app/templates/` — HTML templates

If you want, I can add a `requirements.txt`, example data, or expand these instructions.