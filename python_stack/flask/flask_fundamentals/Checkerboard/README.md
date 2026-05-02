# Checkerboard Flask App

A dynamic Flask web application that generates customizable checkerboards with configurable dimensions and colors.

## Features

- **Dynamic Board Generation**: Create checkerboards with custom rows and columns
- **Color Customization**: Choose two colors for alternating squares
- **Multiple Routes**: Access pre-configured or fully customized boards
- **Responsive Design**: Clean, centered layout using CSS Grid

## Installation

1. Ensure you have Python installed on your system
2. Install Flask:
   ```bash
   pip install flask
   ```

## Running the App

1. Navigate to the project directory
2. Run the Flask application:
   ```bash
   python main.py
   ```
3. Open your browser and visit `http://localhost:5000`

## Routes

### Default Board
- **URL**: `/`
- **Description**: Displays an 8x8 checkerboard with brown and white colors
- **Example**: `http://localhost:5000/`

### Custom Columns
- **URL**: `/<cols>`
- **Description**: Displays an 8-row checkerboard with a custom number of columns
- **Example**: `http://localhost:5000/10`

### Custom Dimensions
- **URL**: `/<rows>/<cols>`
- **Description**: Displays a checkerboard with custom rows and columns
- **Example**: `http://localhost:5000/5/10`

### Fully Customized
- **URL**: `/<rows>/<cols>/<color1>/<color2>`
- **Description**: Displays a checkerboard with custom dimensions and colors
- **Example**: `http://localhost:5000/6/6/red/black`

## Project Structure

```
├── main.py              # Flask application with route definitions
├── templates/
│   └── board.html       # HTML template for rendering the board
├── static/
│   └── css/
│       └── style.css    # Stylesheet for board layout and styling
└── README.md            # This file
```

## Technologies Used

- **Flask**: Lightweight web framework for Python
- **Jinja2**: Template engine for dynamic HTML generation
- **CSS Grid**: Modern layout system for the checkerboard

## Notes

- Each square on the board is 60x60 pixels
- Colors follow web color naming conventions (e.g., red, blue, brown, white)
- The board is automatically centered on the page
