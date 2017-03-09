from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("survey.html")


@app.route('/submit', methods=['POST'])
def survey_submit():
    print "Submitted Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
     if len(name) or len(comment)< 1:
        if len(name)< 1: flash("Name cannot be empty!")
        elif len(comment)<1:flash("Comment cannot be empty!")
    elif len(comment)> 120: flash("Comment can be no longer than 120 characters")
    else:
        flash("Success! Your name is {}".format(name) # just pass a string to the flash function
    return render_template("submit.html", name=name, location=location, language=language, comment=comment)


app.run(debug=True)
