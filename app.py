from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import *


@app.route("/")
def ping():
	return "ping resp"
#register and login
@app.route("/register",methods=['POST'])
def register():
	email_ = request.form['email']
	password_ = request.form['password']
	name_ = request.form['name']
	location_ = request.form['location']
	gender_ = request.form['gender']
	interest_ = request.form['interest']
	college_ = request.form['college']
	print(email_)
	print(password_)
	try:
		#credentials = Credentials(email = email_, password = password_)
		#db.session.add(credentials)
		#db.session.commit()
		profile = Profile(email = email_,name = name_,location = location_,gender = gender_,interest = interest_,college = college_)
		db.session.add(profile)
		db.session.commit()
		return"ok"
		
	except Exception as e:
		return str(e)

@app.route("/login")
def login():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			return True
		else:
			return False
	except Exception as e:
		print(str(e))
		return False
#setter functions

@app.route("/enroll")
def enroll():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			enrollment = Enrollment(
					mentee = email,
					mentor = request.form['mentor'],
					status = False,
					topic_name = request.form['topic_name']
				)
			notif = Notification(
					mentee = email,
					mentor = request.form['mentor'],
					status = False,
					topic_name = request.form['topic_name']
				)
			db.session.add(enrollment)
			db.session.commit()
			db.session.add(notif)
			db.session.commit()
			return True
		else:
			return False
	except Exception as e:
		print(str(e))
		return False
@app.route("/add_timeline")
def add_timeline():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			timeline = Timeline(
					name = request.form['name'],
					day = request.form['day'],
					goal = request.form['goal']
				)
			db.session.add(timeline)
			db.session.commit()
			return True
		else:
			return False
	except Exception as e:
		print(str(e))
		return False
@app.route("/add_mentor")
def add_mentor():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			mentor = Mentor(
					name = request.form['name'],
					email = request.form['email']
				)
			db.session.add(mentor)
			db.session.commit()
			return True
		else:
			return False
	except Exception as e:
		print(str(e))
		return False
@app.route("/add_topics")
def new_topic():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials.password:
			topic = Topic(
					name = request.form['name']
				)
			db.session.add(mentor)
			db.session.commit()
			return True
		else:
			return False
	except Exception as e:
		print(str(e))
		return False
#getter functions

@app.route("/profile")
def profile():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			profile = Profile.query.filter_by(email = email).first()
			print(str(profile))
			dict={
					"email": str(profile.email),
					"name": str(profile.name),
					"interest": str(profile.interest),
					"location": str(profile.location),
					"gender" :str(profile.gender),
					"college": str(profile.college)
				}
			return jsonify(dict)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)
migrate = Migrate(app, db)
if __name__ == '__main__':
	app.run()
#localhost:5000/register?email="root"&password="root"&name="qwerty"&location="qwerty"&gender="male"&interest="qwerty"&college="qwerty"
#curl -v -H "Content-Type: application/json" -X POST \ -d '{"email":"root","password":"root","name":"qwerty","location":"qwerty","gender":"male","interest":"qwerty","college":"qwerty"}' http://127.0.0.1:5000/register