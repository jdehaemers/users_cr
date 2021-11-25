from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
secret_key = 'kajgkjafsg'

@app.route('/')
def load():
    return redirect('/create')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
        }
    User.save(data)
    return redirect('/read')

@app.route('/read')
def read():
    users = User.get_all()
    return render_template('read.html', users=users)

if __name__=="__main__":
    app.run(debug=True)

