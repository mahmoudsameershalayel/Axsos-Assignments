from flask import Flask, render_template, session, redirect, request, jsonify
from itsdangerous import BadSignature

app = Flask(__name__)
app.secret_key = "This is the secret key for our counter app -- SHOULD BE STRONG STRING"

@app.route('/')
def root():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
        
    return render_template(
        'index.html',
        counter = session['counter'],
        visits = session['visits']
    )
    
@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.pop('counter', None)
    return redirect('/')

@app.route('/increment_by_two', methods=['POST'])
def increment_by_two():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    increment_amount = int(request.form['increment_amount'])

    if 'counter' in session:
        session['counter'] += increment_amount - 1
    else:
        session['counter'] = increment_amount - 1

    return redirect('/')

@app.route('/decode_cookie')
def decode_cookie():
    cookie_name = app.config['SESSION_COOKIE_NAME']
    cookie_value = request.cookies.get(cookie_name)

    if not cookie_value:
        return jsonify({
            'message': 'No session cookie found. Visit the home page first.'
        })

    serializer = app.session_interface.get_signing_serializer(app)

    try:
        decoded_cookie = serializer.loads(cookie_value)
    except BadSignature:
        return jsonify({
            'message': 'The session cookie signature is not valid.'
        })

    return jsonify({
        'cookie_name': cookie_name,
        'cookie_value': cookie_value,
        'decoded_cookie': decoded_cookie
    })


    
if(__name__ == "__main__"):
    app.run(debug=True)
