# Ninja Gold

A Django mini-game where a ninja earns gold by visiting locations.

## Setup

```bash
source ../django_env/Scripts/activate
python manage.py migrate
python manage.py runserver
```

Visit `http://localhost:8000`

## How to Play

Choose a location to find gold:

| Location | Gold |
|----------|------|
| Farm     | +10 to +20 |
| Cave     | +10 to +20 |
| House    | +10 to +20 |
| Quest    | -50 to +50 |

Your gold total and activity log are saved in the session.
