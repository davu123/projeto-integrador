from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Configuração da conexão com SQL Server
server = 'localhost'           
database = 'nome_do_banco'     
username = 'seu_usuario'       
password = 'sua_senha'         
driver = 'ODBC Driver 17 for SQL Server'

conn_str = f'''
    DRIVER={{{driver}}};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    TrustServerCertificate=yes;
'''

# Rota de teste
@app.route('/')
def home():
    return "API Flask conectada ao SQL Server!"

# Rota para listar usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email, data_cadastro FROM usuarios")
        rows = cursor.fetchall()
        usuarios = [
            {
                "id": row.id,
                "nome": row.nome,
                "email": row.email,
                "data_cadastro": row.data_cadastro.strftime('%Y-%m-%d %H:%M:%S')
            }
            for row in rows
        ]
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Rota para cadastrar um novo usuário
@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    if not all([nome, email, senha]):
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, email, senha)
            VALUES (?, ?, ?)
        """, (nome, email, senha))
        conn.commit()
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
