from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Credentials(db.Model):
	__tablename__ = 'credentials'
	email = db.Column(db.String(),primary_key=True)
	password = db.Column(db.String())
	def __repr__(self):
		return '<Email %r>' % self.email
	def __init__(self, email, password):
		self.email = email
		self.password = password

class Profile(db.Model):
	__tablename__ = 'profile'
	email = db.Column(db.String(), primary_key = True)
	college = db.Column(db.String())
	interest = db.Column(db.String())
	gender = db.Column(db.String())
	location = db.Column(db.String())
	def __repr__(self):
		return '<Email %r>' % self.email



class Topics(db.Model):
	__tablename__ = 'topics'
	name = db.Column(db.String(), primary_key = True)

class Mentor_list(db.Model):
	__tablename__ = 'mentor_list'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(), ForeignKey('topics.name'))
	email = db.Column(db.String(), ForeignKey('profile.email'))
	profile = relationship("Profile", backref=("profile"))
	topics = relationship("Topics", backref=("topics"))

class Timeline(db.Model):
	__tablename__ = 'timeline'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(), ForeignKey('topics.name'))
	day = db.Column(db.String())
	goal = db.Column(db.String())

class Enrollment(db.Model):
	__tablename__ = 'enrollment'
	id = db.Column(db.Integer, primary_key = True)
	topic_name = db.Column(db.String(), ForeignKey('topics.name'))
	mentor = db.Column(db.String(), ForeignKey('profile.email'))
	mentee = email = db.Column(db.String(), ForeignKey('profile.email'))
	profile = relationship("Profile", backref=("profile"))
	topics = relationship("Topics", backref=("topics"))

class Notification(db.Model):
	__tablename__ = 'notification'
	id = db.Column(db.Integer, primary_key = True)
	mentee = db.Column(db.String(), ForeignKey('profile.email'))
	mentor = db.Column(db.String(), ForeignKey('profile.email'))
	request = db.Column(db.Boolean)
	number = db.Column(db.Integer,primary_key=True)
