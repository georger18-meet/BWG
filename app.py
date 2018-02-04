from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='this is super secret dude!..and really essential'
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/bwg.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True)
	username = db.Column(db.String(80),nullable=False)
	password = db.Column(db.String(99), nullable=False)


@app.route('/') #Display first page, which we can use to sign in/up. 
def firstPage():
	return render_template('Login.html')


@app.route('/home', methods=['POST','GET'])
def home():
	user = User()
	user.email = request.form['email']
	user.username = request.form['uname']
	user.password = request.form['psw']
	db.session.add(user)
	db.session.commit()
	return render_template('Home.html',user = user)

@app.route('/login', methods=['POST'])
def login():
	user = User.query.filter_by(username=request.form['uname'],password=request.form['psw']).first()
	if user!=None :
		return render_template('Home.html',user=user)
	flash('Incorrect username/password')
	return redirect(url_for('firstPage')) 

@app.route('/signup',methods=['POST'])
def signup():
	user = User()
	user.email = request.form['email']
	user.username = request.form['uname']
	user.password = request.form['psw']
	db.session.add(user)
	db.session.commit()
	return render_template('Home.html',user = user)

@app.route('/logout')
def logout():
	return redirect('/')

@app.route('/snakegame')
def snakegame():
	return render_template('Snake.html')

@app.route('/about')
def about():
	return render_template('About.html')


db.create_all()


if __name__ == "__main__":
	app.run()
