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
	email = request.args.get('email')
	password = request.args.get('password')
	name = request.args.get('name')
	location = request.args.get('location')
	gender = request.args.get('gender')
	interest = request.args.get('interest')
	college = request.args.get('college')
	try:
		credentials = Credentials(
			email = email,
			password = password
		)
		db.sesssion.add(credentials)
		db.session.commit()
		profile = Profile(
				email = email,
				name = name,
				location = location,
				gender = gender,
				interest = interest,
				college = college
			)
		db.session.add(profile)
		db.session.commit()
		return"ok"
		
	except Exception as e:
		return str(e)

@app.route("/login")
def login():
	email = request.args.get('email')
	password = request.args.get('password')
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
	email = request.args.get('email')
	password = request.args.get('password')
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			enrollment = Enrollment(
					mentee = email,
					mentor = request.args.get('mentor'),
					status = False,
					topic_name = request.args.get('topic_name')
				)
			notif = Notification(
					mentee = email,
					mentor = request.args.get('mentor'),
					status = False,
					topic_name = request.args.get('topic_name')
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
	email = request.args.get('email')
	password = request.args.get('password')
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			timeline = Timeline(
					name = request.args.get('name'),
					day = request.args.get('day'),
					goal = request.args.get('goal')
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
	email = request.args.get('email')
	password = request.args.get('password')
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			mentor = Mentor(
					name = request.args.get('name'),
					email = request.args.get('email')
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
	email = request.args.get('email')
	password = request.args.get('password')
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			topic = Topic(
					name = request.args.get('name')
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
	email = request.args.get('email')
	password = request.args.get('password')
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == credentials['password']:
			profile = Profile.query.filter_by(email = email).first()
			return jsonify(profile.serialize())
			print (str(profile))
		else:
			return None
	except Exception as e:
		print(str(e))
		return None
migrate = Migrate(app, db)
if __name__ == '__main__':
	app.run()
#localhost:5000/register?email=root&password=root&name=qwerty&location='qwerty'&gender=male&interest=qwerty&college=qwerty