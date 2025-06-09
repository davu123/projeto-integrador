# 💻 Projeto Integrador – Sistema de Cadastro e Login

Este é um sistema web funcional desenvolvido como Projeto Integrador, que permite **cadastro e login de usuários**, com uso de **Flask** no back-end, **SQL Server** como banco de dados, e um **front-end personalizado com HTML, CSS e JavaScript**.

![Tela de Login](https://user-images.githubusercontent.com/seu-usuario/tela-login.png) <!-- Substituir com o link real se desejar -->

---

## ✨ Funcionalidades

✅ Cadastro de novos usuários  
✅ Login com verificação de e-mail e senha  
✅ Sessão de boas-vindas personalizada  
✅ Logout com limpeza de sessão  
✅ Validação de campos no front-end com JavaScript  
✅ Estilo moderno com tema escuro em azul gradiente

---

## 🧰 Tecnologias Utilizadas

| Camada        | Tecnologias                                 |
|---------------|----------------------------------------------|
| Front-end     | HTML5, CSS3, JavaScript Vanilla              |
| Back-end      | Python 3.x, Flask                            |
| Banco de Dados| SQL Server + pyodbc                          |
| Sessão        | Flask session (`session`)                    |

---

## 📁 Estrutura do Projeto

```
projeto-integrador/
│
├── app.py                      # Arquivo principal da aplicação Flask
├── templates/                  # HTMLs renderizados com Jinja2
│   ├── login.html
│   ├── cadastrar.html
│   └── paginainicial.html
├── static/
│   └── js/
│       └── script.js           # Validação de formulário
└── README.md                   # Este documento
```

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/davu123/projeto-integrador.git
cd projeto-integrador
```

### 2. Instale as dependências Python
```bash
pip install flask pyodbc
```

### 3. Configure o banco SQL Server
Use este script para criar a tabela:

```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) UNIQUE NOT NULL,
    senha NVARCHAR(255) NOT NULL,
    data_cadastro DATETIME DEFAULT GETDATE()
);
```

> Altere `app.py` com sua string de conexão personalizada

### 4. Execute a aplicação
```bash
python app.py
```

### 5. Acesse em:
```
http://localhost:5000
```

---

## 🔐 Melhorias Futuras

- Criptografia de senha com `bcrypt`
- Upload de arquivos para justificativa de ponto
- Painel de administração
- Integração com APIs externas
- Testes automatizados com `pytest`

---

## 👨‍🏫 Apresentação Acadêmica

Este projeto foi desenvolvido como parte da disciplina de **Projeto Integrador**, e pode ser apresentado com foco em:

- Conceitos de desenvolvimento web full stack
- Boas práticas de UI/UX
- Integração com banco de dados real
- Validação no front-end e back-end

---

## 👨‍💻 Autores

Desenvolvido por **Davi Oliveira Maia, Cayo Zickler e Gabriel Curvello**  

---

> Para sugestões, contribuições ou dúvidas, abra uma issue ou envie um pull request.
