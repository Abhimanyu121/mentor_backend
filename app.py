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

@app.route("/register")
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
		print(str(e))

@app.route("/login")
def login():
	email = request.args.get('email')
	password = request.args.get('password')
	try:
		credentials=Credentials.query.filter_by(id=id_).first()
		if password == credentials['password']:
			return True
		else
			return False
	except Exception as e:
		print(str(e))
		return False


migrate = Migrate(app, db)
if __name__ == '__main__':
	app.run()
	