from app import db
from sqlalchemy import Table, Column, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

class Credentials(db.Model):
	__tablename__ = 'credentials'
	email = db.Column(db.String(),primary_key=True)
	password = db.Column(db.String())
	
class User_Profile(db.Model):
	__tablename__ = 'user_profile'
	email = db.Column(db.String(), primary_key = True)
	college = db.Column(db.String())
	interest = db.Column(db.String())
	gender = db.Column(db.String())
	location = db.Column(db.String())
	name = db.Column(db.String())
	mentor = db.Column(db.Boolean)
#	mentors = db.relationship("Mentor_list", backref="profile-mentor", lazy='dynamic')
#	enroll = db.relationship("Enrollment", backref="profile-enroll", lazy='dynamic')
#	notifs = db.relationship("Notification", backref="profile-notifs", lazy='dynamic')
#	time = db.relationship("Timeline", backref="profile-time", lazy='dynamic')




class Topics(db.Model):
	__tablename__ = 'topics'
	topic_name = db.Column(db.String(), primary_key = 'dynamic')
#	mentors = db.relationship("Mentor_list", backref="topic-mentor", lazy='dynamic')
#	time = db.relationship("Timeline", backref="topics-time", lazy='dynamic')
#	enroll = db.relationship("Enrollment", backref="topics-enroll", lazy='dynamic')
#	notifs = db.relationship("Notification", backref="topics-notifs", lazy='dynamic')
class Mentor_list(db.Model):
	__tablename__ = 'mentor_list'
	id = db.Column(db.Integer, primary_key = True)
	topic_name = db.Column(db.String(), db.ForeignKey('topics.topic_name'))
	email = db.Column(db.String(), db.ForeignKey('user_profile.email'))

class Timeline(db.Model):
	__tablename__ = 'timeline'
	id = db.Column(db.Integer, primary_key = True)
	topic_name = db.Column(db.String(),db.ForeignKey('topics.topic_name'))
	day = db.Column(db.String())
	goal = db.Column(db.String())
	mentor = db.Column(db.String(),db.ForeignKey('user_profile.email'))
#	db.ForeignKeyConstraint(['name','mentor'], ['topics.topic_name','user_profile.email'])

class Enrollment(db.Model):
	__tablename__ = 'enrollment'
	id = db.Column(db.Integer, primary_key = True,autoincrement=True)
	topic_name = db.Column(db.String(),db.ForeignKey('topics.topic_name'))
	mentor = db.Column(db.String(),db.ForeignKey('user_profile.email'))
	mentee = db.Column(db.String(),db.ForeignKey('user_profile.email'))
	status = db.Column(db.Integer)#1=requested 2=stuff going on 3 = stuff over
#	db.ForeignKeyConstraint(['mentor', 'mentee', ' topic_name'], ['user_profile.email', 'user_profile.email','topics.topic_name'])
class Notification(db.Model):
	__tablename__ = 'notification'
	topic_name = db.Column(db.String(),db.ForeignKey('topics.topic_name'))
	sender = db.Column(db.String(),db.ForeignKey('user_profile.email'))#sender
	recipient = db.Column(db.String(),db.ForeignKey('user_profile.email'))#recipient
	request = db.Column(db.Boolean)
	number = db.Column(db.Integer,primary_key=True)
#	db.ForeignKeyConstraint(['mentor', 'mentee', ' topic_name'], ['user_profile.email', 'user_profile.email','topics.topic_name'])
class New_requests(db.Model):
	__tablename__='request_list'
	topic_name = db.Column(db.String())
	id = db.Column(db.Integer,primary_key=True)
	requester = db.Column(db.String(),db.ForeignKey('user_profile.email'))