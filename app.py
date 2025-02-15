from flask import Flask, render_template, request, jsonify
from chatbot import agent

app = Flask(__name__)

chat_agent = agent()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.json['message']
        response = chat_agent.run(user_message)
        return jsonify({'response': response})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
