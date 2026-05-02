# Playground Flask App

A simple Flask app that displays boxes/cards using dynamic routes.

## Setup

Install Flask:

```bash
pip install flask
```

## Run

Start the app:

```bash
python main.py
```

Open the app in your browser:

```text
http://localhost:5000/play
```

## Routes

- `/play` shows 3 aqua cards.
- `/play/<nums>` shows the number of aqua cards you choose.
- `/play/<nums>/<color>` shows the number and color of cards you choose.

## Examples

- `http://localhost:5000/play`
- `http://localhost:5000/play/5`
- `http://localhost:5000/play/5/red`
