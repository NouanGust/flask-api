# Importações
from flask import Flask, make_response, jsonify, request
import sqlite3

# Iniciando o Flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Funções da API

# GET
# Decorator do Flask(rota, função) -- o @ marca a linha debaixo para criar uma rota da API
@app.route('/jogos', methods=['GET'])
def get_jogos():
    
    # Conectando com o banco
    
    conn = sqlite3.connect('jogos_dados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jogos")
    resultados = cursor.fetchall()
    conn.close()

    return jsonify(resultados)


# Post
@app.route('/jogos', methods=['POST'])
def create_jogo():
    jogo = request.json
    # Conectar no banco
    conn = sqlite3.connect('jogos_dados.db')
    cursor = conn.cursor()
    
    # Inserindo dados
    cursor.execute("INSERT INTO jogos (genero, nome, plataforma, ano) VALUES (?, ?, ?, ?)", (jogo['genero'], jogo['nome'], jogo['plataforma'], jogo['ano']))
    
    conn.commit()
    conn.close()
    return jsonify(jogo), 201


# Update
@app.route('/alterar/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    jogo = request.json
    
    # Conectando com o banco
    conn = sqlite3.connect('jogos_dados.db')
    cursor = conn.cursor()
    
    # Alterando dados
    cursor.execute("""
                   UPDATE jogos 
                   SET genero = ?, nome = ?, plataforma = ?, ano = ?  
                   WHERE id = ?
                   """, (jogo['genero'], jogo['nome'], jogo['plataforma'], jogo['ano'], id))
    
    # Confirmando a operação
    conn.commit()
    
    # Fechando a conexão
    conn.close()
    
    if cursor.rowcount == 0:
        return jsonify({"error": "Jogo não encontrado"}), 404
    
    return jsonify(jogo), 200

# Delete
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_jogo(id):
    
    # Conectando com o banco
    conn = sqlite3.connect('jogos_dados.db')
    cursor = conn.cursor()
    
    # Deletando dados
    cursor.execute("DELETE FROM jogos WHERE id = ?", (id,))
    
    conn.commit()
    conn.close()
    
    return '', 204
    


# Rodando
app.run()