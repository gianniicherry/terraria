# chat.py
from flask import Flask, jsonify
from decouple import config
import openai

app = Flask(__name__)

api_key = config("OPENAI_API_KEY")
openai.api_key = api_key

def generate_regions():
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are telling a Fantasy story based on a user's choices"},
            {"role": "user", "content": "Return six randomly generated regions. Please return the name of the region and a description of each region"}
        ],
    )
    return completion.choices[0].message

# Define a Flask route in the same file
@app.route('/api/get_regions', methods=["GET"])
def get_regions():
    try:
        response = generate_regions()
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
