import sqlite3

# Criando e conectando no banco
try:
    conn = sqlite3.connect('jogos_dados.db')
    cursor = conn.cursor()
    
    # Criando uma tabela
    cursor.execute('CREATE TABLE IF NOT EXISTS jogos (id INTEGER PRIMARY KEY, genero TEXT, nome TEXT, plataforma TEXT, ano INTEGER)')
    
    # Inserindo Dados
    # cursor.execute("INSERT INTO jogos (genero, nome, plataforma, ano) VALUES ('Terror/Survival Horror', 'Resident Evil 2', 'PS4', 2019)")
    # cursor.execute("INSERT INTO jogos (genero, nome, plataforma, ano) VALUES ('Terror/Survival Horror', 'Resid2 Evil 2', 'PS4', 2013)")
    
    # Confirmando a transação
    conn.commit()
    
except sqlite3.Error as e:
    print(f"Erro ao acessar o banco de dados: {e}")
finally:
    # Fechando a conexão com o banco de dados
    if conn:
        conn.close()
