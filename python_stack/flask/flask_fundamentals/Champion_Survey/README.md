# Champion Survey

A simple Flask web app that collects a developer survey and displays the submitted results.

## Features

- Survey form with name, location, favorite language, experience level, technologies, and comment fields
- Results page showing all submitted data
- Back button to return to the survey form

## Setup

1. Install dependencies:
   ```bash
   pip install flask
   ```

2. Run the app:
   ```bash
   python main.py
   ```

3. Open your browser at `http://127.0.0.1:5000`

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Survey form |
| `/result` | POST | Submitted results page |
