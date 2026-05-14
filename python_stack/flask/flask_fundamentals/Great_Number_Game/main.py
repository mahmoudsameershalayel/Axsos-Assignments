from flask import Flask, render_template, request, redirect, session
import random  
app = Flask(__name__)
app.secret_key = 'Great@11#2Number%^$Game&&*Secret'
leaderboard = []

@app.route('/')
def main_page():
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)  

    if 'attempts' not in session:
        session['attempts'] = 0

    print(session['random_number'])
    return render_template(
        'index.html',
        result=session.get('result'),
        attempts=session.get('attempts')
    )
@app.route('/guess', methods=['POST'])
def guessed_number():
    guessed_number = int(request.form['guessed_number'])
    random_number = session['random_number']
    session['attempts'] = session.get('attempts', 0) + 1
    
    if guessed_number == random_number:
        session['result'] = 'correct'
    elif guessed_number > random_number:
        session['result'] = 'high'
    else:
        session['result'] = 'low'

    if session['result'] != 'correct' and session['attempts'] >= 5:
        session['result'] = "lose"

    return redirect('/')

@app.route('/winner', methods=['POST'])
def save_winner():
    if session.get('result') != 'correct':
        return redirect('/')

    name = request.form['name'].strip()

    if name:
        leaderboard.append({
            'name': name,
            'attempts': session.get('attempts', 0)
        })

    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard_page():
    sorted_winners = sorted(leaderboard, key=lambda winner: winner['attempts'])
    return render_template('leaderboard.html', winners=sorted_winners)
    
@app.route('/reset')
def reset():
    session.pop('random_number', None)
    session.pop('attempts', None)
    session.pop('result', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
