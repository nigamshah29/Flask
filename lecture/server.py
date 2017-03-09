from flask import Flask, render_template, redirect, session, flash, request

app = Flask(__name__)
app.secret_key = 'some secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_york')
def new_york():
    if 'trip_history' in session:
        history = session['trip_history']
        history.insert(0, 'visited New York')
        session['trip_history'] = history
    return render_template('NewYork.html')

@app.route('/Indiana')
def indiana():
    if 'trip_history' in session:
        history = session['trip_history']
        history.insert(0, 'visited Indiana')
        session['trip_history'] = history
    return render_template('Indiana.html')

@app.route('/California')
def california():
    if 'trip_history' in session:
        history = session['trip_history']
        history.insert(0, 'visited California')
        session['trip_history'] = history
    return render_template('California.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    server_email = request.form['html_email']
    server_password = request.form['html_password']
    if (server_email=='user@gmail.com' and server_password=='abcdabcd'):
        session['user_name'] = server_email[:4]
        session['email'] = server_email
        session['trip_history'] = []
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
