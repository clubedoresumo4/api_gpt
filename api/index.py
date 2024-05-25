from flask import Flask, request, jsonify
from g4f.client import Client
import random
import requests

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
        proxies = requests.get("https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=1&sort_by=lastChecked&sort_type=desc")
        proxies = proxies.json()
        data = proxies['data']
        total = proxies['total']
        
        aleatorio = random.randint(0,total)
        proxy = data[aleatorio]        
        proxy = "http://181.233.93.88:8080"
        G4F_PROXY=proxy
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
