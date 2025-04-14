from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'segredo-super-seguro'

DB_PATH = 'database.db'

# --- Funções auxiliares ---
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

# --- Rotas ---
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['usuario'] = user[1]  # nome
            return redirect(url_for('paginainicial'))
        else:
            flash('E-mail ou senha inválidos')
    return render_template('login.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
            conn.commit()
            conn.close()
            flash('Cadastro realizado com sucesso!')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('E-mail já cadastrado.')
    return render_template('cadastrar.html')

@app.route('/paginainicial')
def paginainicial():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('paginainicial.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
