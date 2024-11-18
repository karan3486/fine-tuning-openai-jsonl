from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
client = OpenAI()
# Configure your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to get the response from the model
def get_answer(question):
  response=client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:personal::AFEV9Ozr",
    messages=[
        {"role": "user", "content": question}
    ]
  )
  return response.choices[0].message.content

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle chatbot messages
@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = get_answer(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
