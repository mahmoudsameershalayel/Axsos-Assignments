# Dojo Survey

A simple Django survey form that collects user information and displays the results.

## Features

- Survey form with name, location, language, experience level, interests, and comment fields
- Result page displaying submitted data
- Bootstrap 5 styling

## Setup

```bash
# Activate virtual environment
source django_env/Scripts/activate  # Windows: django_env\Scripts\activate

# Run the server
python manage.py runserver
```

## Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `index` | Survey form |
| `/survey` | `submit_survey` | Handles form submission |
| `/result` | `show_result` | Displays results |
