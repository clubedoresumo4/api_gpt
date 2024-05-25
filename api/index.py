from flask import Flask, request, jsonify
from g4f.client import Client
from g4f.cookies import set_cookies
app = Flask(__name__)


set_cookies(".google.com", {
  "__Secure-1PSIDCC": "AKEyXzUPG7_1fAQjMLNE_PMoVqhfTswE53e_p0ibIJeFFyvjpd9iAGj1PtvilZqjKe3f4_sm0Q",
  "__Secure-1PSIDTS": "sidts-CjEBLwcBXDGRKlxKI6aFGQG5DvxSOAOYomOSXSQ6OI6HbRh1c3SzPFG2UyZDdu9RWa4AEAA",
  "__Secure-1PSID":"g.a000kAikKfidrFdIUqxvSZqS8p_jUkiEp3tgXBea-ObFbHY45LRdMfzaxJyu4v5-jTH1XhyqygACgYKATASARYSFQHGX2Miq87l-Z8ddHn1HvDg_vZNYRoVAUF8yKoB_OqyY_K9n3kG3ro4EMcO0076"
})
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
            model="gemini",
            messages=[{"role": "user", "content": f'''{question}'''}],
        )    
        return jsonify({'resposta': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/about')
def about():
    return 'About'
