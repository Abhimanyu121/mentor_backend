from app import db

class Credentials(db.Model):
	__tablename__ = 'credentials'
	email = db.column(db.String(), primary_key = true)
	password = db.column(db.String())
	def __repr__(self):
		return '<Email %r>' % self.email

    def __init__(self, email, password ):
        self.email = email
        self.password = password

class Profile(db.model):
	__tablename__ = 'profile'
	email = db.column(db.String(), primary_key = true)
	college = db.column(db.String())
	interest = db.column(db.String())
	gender = db.column(db.String())
	location = db.column(db.String())
	def __repr__(self):
		return '<Email %r>' % self.email



class Topics(db.model):
	__tablename__ = 'topics'
	name = db.column(db.String(), primary_key = true)

class Mentor_list(db.model):
	__tablename__ = 'mentor_list'
	name = db.column(db.String(), ForeignKey('topics.name'))
	email = db.column(db.String(), ForeignKey('profile.email'))
	profile = relationship("Profile", backref=backref("profile", uselist=False))
	topics = relationship("Topics", backref=backref("topics", uselist=False))

class Timeline(db.model):
	__tablename__ = 'timeline'
	name = db.column(db.String(), ForeignKey('topics.name'))
	day = db.column(db.String())
	goal = db.column(db.String())

class Enrollment(db.model):
	__tablename__ = 'enrollment'
	topic_name = db.column(db.String(), ForeignKey('topics.name'))
	mentor = db.column(db.String(), ForeignKey('profile.email'))
	mentee = email = db.column(db.String(), ForeignKey('profile.email'))
	profile = relationship("Profile", backref=backref("profile", uselist=False))
	topics = relationship("Topics", backref=backref("topics", uselist=False))

class Notification(db.model):
	__tablename__ = 'notification'
	mentee = db.column(db.String(), ForeignKey('profile.email'))
	mentor = db.column(db.String(), ForeignKey('profile.email'))
	request = db.column(db.Boolean)
	number = db.column(db.Integer, Sequence(increment=1),primary_key=True)
