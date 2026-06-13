# Login and Registration

A Django web application with user registration and login functionality.

## Features

- User registration with server-side validation
- Login with bcrypt password hashing
- Session-based authentication
- Protected success page

## Validation Rules

- First and last name: minimum 2 characters
- Email: valid format, must be unique
- Password: minimum 8 characters, must match confirmation
- Birth date: must be in the past, user must be at least 13 years old

## Setup

1. Install dependencies:
   ```bash
   pip install django bcrypt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the server:
   ```bash
   python manage.py runserver
   ```

4. Visit `http://localhost:8000`

## Tech Stack

- Python / Django
- SQLite
- bcrypt for password hashing
