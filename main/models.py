from datetime import datetime
from __main__ import db

class User(db.Model): # class models representative/creating SQL DB fields
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False) # if null is true means field doesn't need to be filled
    email = db.Column(db.String(80), unique=True, nullable=False) # number is field length (80 string characters)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # Post is the class below (hence capital), backref is like adding another column to Post saying who wrote the post, using author
    # returns all the User return info below, lazy loading is load object one before object 2 (parent child relationship).

    def __repr__(self): # what we want a user to print when we print a user
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #primary key of the User so its a ForeignKey.
    # But why is Post in Post class uppercase and this lover case? Because that references the CLASS Post and this references a column (id)
    # within the table, and by default table names are the Class name, so it is lower case despite mentioning the class.
    # If it referenced just the Class it be upper and we can change the table name if we choose

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
