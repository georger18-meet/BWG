from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/bwg.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True)
	username = db.Column(db.String(80),nullable=False)
	password = db.Column(db.String(99), nullable=False)


@app.route('/home', methods=['POST','GET'])
def home():
	user = User()
	user.email = request.form['email']
	user.username = request.form['uname']
	user.password = request.form['psw']
	db.session.add(user)
	db.session.commit()
	return render_template('Home.html',user = user)



@app.route('/')
def signup():
	return render_template('Login.html')

@app.route('/logout')
def logout():
	return redirect('/')


db.create_all()


if __name__ == "__main__":
	app.run()
