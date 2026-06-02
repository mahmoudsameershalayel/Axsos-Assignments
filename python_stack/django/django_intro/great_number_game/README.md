# Great Number Game

A Django guessing game where the server picks a random number between 1 and 100 and the player tries to guess it.

## How to play

1. Visit `/` — a secret number is stored in your session
2. Submit a guess — you'll be told if it's **too high**, **too low**, or **correct**
3. You have **5 attempts** before the number is revealed and you lose
4. On a win, enter your name to appear on the leaderboard

## Routes

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Home — starts a new game if no session exists |
| `/guess` | POST | Processes a guess and returns feedback |
| `/submit_winner` | POST | Saves winner's name and redirects to leaderboard |
| `/leaderboard` | GET | Shows all winners sorted by fewest attempts |

## Setup

```bash
# Activate your virtual environment, then:
python manage.py migrate
python manage.py runserver
```
