import requests
from flask import jsonify, Blueprint, request
#from config import app

service_bp = Blueprint('service_bp', __name__)

@service_bp.route('/teste', methods=['GET'])
def testa():
    url = "http://localhost:5001/reservas"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança erro se status != 200
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500

@service_bp.route('/reservas', methods=[])
def validar_turma():
    url = "http://localhost:5001/reservas"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança erro se status != 200
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500

@service_bp.route("/reservas", methods=["POST"])
def cria_reserva():
    url = "http://localhost:5001/reservas"
    dados = request.get_json()
    try:
        resposta = requests.post(url, json=dados)
        resposta.raise_for_status()  # Lança erro se status != 200
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500

@service_bp.route("/reservas", methods=["GET"])
def le_reservas():
    url = "http://localhost:5001/reservas"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança erro se status != 200
        dados = resposta.json()
        return jsonify(dados)
    
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500
    
@service_bp.route('/reservas/<int:id_reserva>', methods=['GET'])
def le_reservas_id(id_reserva):
    url = f"http://localhost:5001/reservas/{id_reserva}"  # Aqui é a correção
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        return jsonify(dados)
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao acessar a API externa', 'detalhes': str(e)}), 500
