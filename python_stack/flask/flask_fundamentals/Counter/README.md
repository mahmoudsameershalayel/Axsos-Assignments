# Flask Counter

A simple Flask app that uses session data to track page visits and a counter value.

## Features

- Shows how many times the user visited the page
- Shows the current counter value
- Increments the counter when the page is refreshed
- Adds `+2` with a button
- Resets only the counter
- Allows the user to choose a custom increment amount
- Decodes the Flask session cookie for learning purposes

## Run The App

```bash
python server.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Routes

- `/` - displays the page and updates visits/counter
- `/increment_by_two` - increments the counter by 2
- `/increment` - increments the counter by the amount entered by the user
- `/destroy_session` - resets the counter
- `/decode_cookie` - displays decoded session cookie information

## Notes

The app uses Flask sessions. Flask stores session data in a signed browser cookie. The cookie can be decoded, but changing it manually will make the signature invalid.
