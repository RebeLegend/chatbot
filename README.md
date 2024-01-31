# Cybersecurity Chatbot

This repository contains a simple Flask-based chatbot application. The chatbot uses a JSON file for predefined question-answer pairs related to cybersecurity. 

## Features
- Case-insensitive matching for user queries.
- Partial matching allows flexibility in how questions are phrased.
- Simple and interactive user interface.

## How It Works
- The Flask backend (`app.py`) loads questions and answers from `qa_data.json`.
- User input is normalized and matched against the questions in the JSON file.
- The frontend (`index.html` and `script.js`) interacts with the user, sending their queries to the backend and displaying responses.

## Setup
1. Clone the repository.
2. Install the required Python packages.
3. Run `app.py` to start the Flask server.
4. Access the chatbot through a web browser.

Feel free to contribute or use this project as a basis for creating more complex chatbot applications!

