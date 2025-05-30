import requests
from flask import jsonify, Blueprint
from config import app

service_bp = Blueprint('service_bp', __name__)

@service_bp.route('/teste', methods=['GET'])
def testa():
    url = "http://localhost:5001/reservas"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500

