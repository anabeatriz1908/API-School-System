import requests
from flask import jsonify, Blueprint, request

api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/reservas", methods=["POST"])
def cria_reserva():
    url = "http://localhost:5001/reservas"
    dados = request.get_json()
    try:
        resposta = requests.post(url, json=dados)
        resposta.raise_for_status()
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500

@api_bp.route("/reservas", methods=["GET"])
def le_reservas():
    url = "http://localhost:5001/reservas"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500
    
@api_bp.route("/reservas/<int:id_reserva>", methods=["GET"])
def le_reservas_id(id_reserva):
    url = f"http://localhost:5001/reservas/{id_reserva}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return jsonify(dados)
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500


@api_bp.route('/atividades', methods=['GET'])
def listar_atividades():
    url = "http://127.0.0.1:5002/atividades"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500

@api_bp.route('/atividades/<int:id_atividade>', methods=['GET'])
def listar_atividade_ID(id_atividade):
    url = f"http://localhost:5002/atividades/{id_atividade}" 
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return jsonify(dados)
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500


@api_bp.route('/atividades', methods=['POST'])
def criar_atividade():
    url = "http://127.0.0.1:5002/atividades"
    dados = request.get_json()
    try:
        resposta = requests.post(url, json=dados)
        resposta.raise_for_status() 
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500