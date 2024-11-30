from flask import Flask, request
from test_url import get_web

app = Flask(__name__)

@app.route("/")
def hello() -> str:    
    return "Hello, World!"

@app.route('/get_web', methods=['GET'])
def get_web_endpoint():
    url = request.args.get('url', 'https://www.emol.com')  # Leer URL del parámetro de consulta
    html_response = get_web(url)
    return html_response

