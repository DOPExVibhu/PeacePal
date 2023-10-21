from flask import Flask, request, jsonify, render_template, send_from_directory
import pandas as pd
from model import SimpleChatbot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = pd.read_csv(r"Mental_Health_FAQ.csv")
questions = data['Questions'].tolist()
answers = data['Answers'].tolist()

chatbot = SimpleChatbot(questions, answers)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/chat', methods=['POST'])
# def chat_endpoint():
#     try:
#         user_input = request.json['user_input']
#         response = chatbot.get_response(user_input)
#         return jsonify({'response': response})
#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({'response': "Sorry, there was an error processing your request."})


@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        user_input = request.json['user_input']
        print(f"Received user input: {user_input}")  # Debugging line
        response = chatbot.get_response(user_input)
        print(f"Generated response: {response}")  # Debugging line
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error: {e}")  # This will print any exception to the terminal
        return jsonify({'response': "Sorry, there was an error processing your request."})


@app.route('/static/<path:filename>')
def staticfiles(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == "__main__":
    app.run(debug=True)
