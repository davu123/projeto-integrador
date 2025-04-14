from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticação
        pass
    return render_template('login.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Lógica de cadastro
        pass
    return render_template('cadastrar.html')

@app.route('/paginainicial')
def paginainicial():
    return render_template('paginainicial.html')

if __name__ == '__main__':
    app.run(debug=True)
