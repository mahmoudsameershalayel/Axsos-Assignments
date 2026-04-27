# Understanding Routing

A simple Flask app for practicing basic routes, dynamic URL parameters, and custom error handling.

## Setup

Install Flask if it is not already installed:

```bash
pip install flask
```

## Run the App

Start the development server:

```bash
python main.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Routes

| Route | Response |
| --- | --- |
| `/` | `Hello World!` |
| `/Champion` | `Champion!` |
| `/say/<name>` | `Hi <name>!` |
| `/repeat/<num>/<word>` | Repeats `word` `num` times |

Examples:

```text
http://127.0.0.1:5000/say/Ahmad
http://127.0.0.1:5000/repeat/3/hello
```

Unknown routes return:

```text
Sorry! No response. Try again.
```
