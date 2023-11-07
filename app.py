from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # SQLite database URL
db = SQLAlchemy(app)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.column(db.String(200),nullable=False)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weapon = db.Column(db.string(100), nullable=False)
    role = db.relationship('Role', backref=db.backref('role', lazy=True))

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    character = db.relationship('Character', backref=db.backref('stories', lazy=True))

@app.route('/create-db')
def create_db():
    db.create_all()  # Creates the database and tables based on the models
    return 'Database created successfully!'

if __name__ == '__main__':
    app.run()
