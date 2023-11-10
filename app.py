from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify
from flask_cors import CORS
from decouple import config
import openai



app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # SQLite database URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api_key = config("OPENAI_API_KEY")

openai.api_key = api_key

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(200),nullable=False)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weapon = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('characters', lazy=True))

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character', backref=db.backref('stories', lazy=True))

@app.route('/create-db')
def create_db():
    db.create_all()  # Creates the database and tables based on the models
    return 'Database created successfully!'


@app.route('/api/roles', methods=['GET'])
def get_roles():
    roles = Role.query.all()  
    role_data = [{'id': role.id, 'name': role.name, 'description': role.description} for role in roles]
    return jsonify(role_data)


if __name__ == '__main__':
    app.run()
