from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/get_answer', methods=['GET'])
def get_answer():
    question = request.args.get('question')
    if not question:
        return jsonify({'error': 'Question parameter is required'}), 400    
    try:
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f'''{question}'''}],
        )    
        return jsonify({'resposta': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/about')
def about():
    return 'About'
