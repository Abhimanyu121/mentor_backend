from app import db
from sqlalchemy import Table, Column, Integer, ForeignKeyConstraint
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

class User_Profile(db.Model):
	__tablename__ = 'user_profile'
	email = db.Column(db.String(), primary_key = True)
	college = db.Column(db.String())
	interest = db.Column(db.String())
	gender = db.Column(db.String())
	location = db.Column(db.String())
	name = db.Column(db.String())
	#mentors = relationship("Mentor_list"))
	#enroll = relationship("Enrollment"))
	#notifs = relationship("Notification"))
	#def __init__(self, email,password):
	#	self.email= email
	#	self.college = college
	#	self.interest = interest
	#	self.gender = gender
	#	self.location = location
	#	self.name = name

	#def __repr__(self):
	#	return '<Email %r>' % self.email



class Topics(db.Model):
	__tablename__ = 'topics'
	topic_name = db.Column(db.String(), primary_key = True)
	#mentors = relationship("Mentor_list")
	#time = relationship("Timeline")
	#enroll = relationship("Enrollment")
	#notifs = relationship("Notification")

class Mentor_list(db.Model):
	__tablename__ = 'mentor_list'
	id = db.Column(db.Integer, primary_key = True)
	topic_name = db.Column(db.String())
	email = db.Column(db.String())
	#ForeignKeyConstraint(['email', 'topic_name'], ['profile.email', 'topics.topic_name'])

class Timeline(db.Model):
	__tablename__ = 'timeline'
	id = db.Column(db.Integer, primary_key = True)
	topic_name = db.Column(db.String())
	day = db.Column(db.String())
	goal = db.Column(db.String())
	#ForeignKeyConstraint(['name'], ['topics.topic_name'])

class Enrollment(db.Model):
	__tablename__ = 'enrollment'
	id = db.Column(db.Integer, primary_key = True)
	topic_name = db.Column(db.String())
	mentor = db.Column(db.String())
	mentee = db.Column(db.String())
	status = db.Column(db.Boolean)
	#ForeignKeyConstraint(['mentor', 'mentee', ' topic_name'], ['profile.email', 'profile.email','topics.topic_name'])
class Notification(db.Model):
	__tablename__ = 'notification'
	id = db.Column(db.Integer, primary_key = True)
	topic_name = db.Column(db.String())
	mentee = db.Column(db.String())
	mentor = db.Column(db.String())
	request = db.Column(db.Boolean)
	number = db.Column(db.Integer,primary_key=True)
	#ForeignKeyConstraint(['mentor', 'mentee', ' topic_name'], ['profile.email', 'profile.email','topics.topic_name'])
