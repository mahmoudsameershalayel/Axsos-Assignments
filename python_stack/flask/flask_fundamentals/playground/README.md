# Card Game Playground

A simple Flask web application to display customizable playing cards.

## Features

- Display playing cards with configurable count and color
- Dynamic URL routing for easy customization
- Built with Flask and Jinja2 templating

## Routes

- `/play` - Display 3 cards in aqua color
- `/play/<nums>` - Display a specified number of cards in aqua color
- `/play/<nums>/<color>` - Display a specified number of cards in a custom color

## Installation

1. Install Flask:
   ```
   pip install flask
   ```

## Running the App

Start the development server:
```
python main.py
```

The app will run on `http://localhost:5000` by default.

## Usage Examples

- `http://localhost:5000/play` - View 3 aqua cards
- `http://localhost:5000/play/5` - View 5 aqua cards
- `http://localhost:5000/play/7/red` - View 7 red cards
