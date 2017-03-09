from flask import Flask, render_template, redirect, session, flash, request

app = Flask(__name__)
app.secret_key = 'some secret key'
import random

@app.route('/')
def index():
    if not 'result' in session:
        session['result'] = None
        session['actual'] = random.randrange(1,101)
    return render_template('home.html')


@app.route('/result', methods=['POST'])
def result():
    userGuess = int(request.form['user_guess'])
    session['result'] = userGuess
    return redirect('/')

@app.route('/playAgain', methods=['POST'])
def playAgain():
    session.clear()
    return redirect('/')

app.run(debug=True)
