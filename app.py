from flask import Flask, jsonify, request, render_template
import json
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load Q&A data
with open('qa_data.json', 'r') as file:
    qa_data = json.load(file)

# Normalize function to process text
def normalize_text(text):
    # Convert text to lowercase and remove non-alphanumeric characters
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

#Route to main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = normalize_text(request.json['message'])
    response = None

    # Search for partial matches
    for question, answer in qa_data.items():
        if user_input in normalize_text(question):
            response = answer
            break

    if not response:
        response = "Sorry, I don't have an answer to that question."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
