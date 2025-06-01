from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Configuração da conexão com SQL Server
server = 'localhost'
database = 'projeto_integrador'
username = 'sa'
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

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO usuarios (nome, email, senha)
                VALUES (?, ?, ?)
            """, (nome, email, senha))
            conn.commit()
            return redirect(url_for('login'))
        except Exception as e:
            return f"Erro ao cadastrar: {e}"

    return render_template('cadastro.html')

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM usuarios WHERE email = ? AND senha = ?
            """, (email, senha))
            usuario = cursor.fetchone()

            if usuario:
                return render_template('index.html', nome=usuario.nome)
            else:
                return "Login inválido"
        except Exception as e:
            return f"Erro ao fazer login: {e}"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
