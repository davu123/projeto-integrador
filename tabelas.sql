-- Tabela principal de usuários
CREATE TABLE usuarios (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) UNIQUE NOT NULL,
    senha NVARCHAR(255) NOT NULL,
    data_cadastro DATETIME DEFAULT GETDATE()
);

-- Endereço do usuário (1 para 1 opcional)
CREATE TABLE enderecos (
    id INT PRIMARY KEY IDENTITY(1,1),
    usuario_id INT FOREIGN KEY REFERENCES usuarios(id),
    rua NVARCHAR(255),
    numero NVARCHAR(50),
    cidade NVARCHAR(100),
    estado NVARCHAR(50),
    cep NVARCHAR(20)
);

-- Logs de acesso dos usuários
CREATE TABLE logs_acesso (
    id INT PRIMARY KEY IDENTITY(1,1),
    usuario_id INT FOREIGN KEY REFERENCES usuarios(id),
    ip NVARCHAR(45),
    data_acesso DATETIME DEFAULT GETDATE()
);

-- Mensagens enviadas por formulário de contato
CREATE TABLE mensagens_contato (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio DATETIME DEFAULT GETDATE()
);

-- Categorias de produtos (caso use e-commerce)
CREATE TABLE categorias (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(100) NOT NULL
);

-- Produtos que podem ser exibidos ou vendidos
CREATE TABLE produtos (
    id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(255) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2),
    categoria_id INT FOREIGN KEY REFERENCES categorias(id),
    data_cadastro DATETIME DEFAULT GETDATE()
);
