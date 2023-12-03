from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify, request
from flask_cors import CORS
from decouple import config
import openai
import subprocess




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

@app.route('/api/regions', methods=['GET'])
def generate_regions():
    # Modify the subprocess call to run your chat.py script
    result = subprocess.run(["python", "chat.py"], capture_output=True, text=True)

    # Get the printed content from the subprocess result
    printed_content = result.stdout.strip()

    return printed_content

@app.route('/api/characters', methods=['POST'])
def create_character():
    data = request.json

    # Extract character information from the request data
    name = data.get('name')
    weapon = data.get('weapon')
    role_name = data.get('role_name')
    region = data.get('region')

    # Validate that required fields are present
    if not name or not weapon or not role_name or not region:
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if the specified role exists by name
    role = Role.query.filter_by(name=role_name).first()
    if not role:
        return jsonify({'error': 'Role not found'}), 404

    # Create a new character instance with the role_id
    character = Character(name=name, weapon=weapon, role_id=role.id)

    # Add the character to the database
    db.session.add(character)
    db.session.commit()

    return jsonify({'message': 'Character created successfully'}), 201


if __name__ == '__main__':
    app.run()
