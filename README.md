# 📊 Teste de Nivelamento

Este projeto foi desenvolvido como parte de um teste técnico e envolve a extração, transformação, armazenamento e exibição de dados de operadoras de saúde. O sistema consiste em:

- **Web Scraping e Transformação de Dados:** Coleta e limpeza dos dados das operadoras.
- **Banco de Dados:** Armazenamento dos dados processados em um banco MySQL.
- **API:** Backend desenvolvido em Python (Flask) para fornecer acesso aos dados.
- **Frontend:** Interface desenvolvida com Vue 3 e Vite para exibir os dados das operadoras.

---

## 🛠 **Tecnologias Utilizadas**

### 📌 Backend:

- **Python 3.10+**
- **Flask** – Framework web para a API
- **Flask-CORS** – Permite requisições do frontend
- **MySQL Connector** – Para conectar ao banco MySQL
- **MySQL** – Banco de dados relacional
- **Pandas, BeautifulSoup, Requests** – Utilizados no web scraping e tratamento de dados

### 🎨 Frontend:

- **Vue 3** – Framework JavaScript
- **Vite** – Ferramenta para build rápida do Vue
- **Axios** – Para consumo da API

---

## 🚀 **Passo a Passo para Configuração**

### 📥 **1. Clonando o Repositório**

````bash
git clone https://github.com/seu-usuario/teste-de-nivelamento.git
````


## 🏗️ Criando o Ambiente Virtual no Python

Antes de instalar as dependências do projeto, é recomendado criar um ambiente virtual para evitar conflitos entre pacotes.

### 📌 Criando o ambiente virtual:

````bash
Execute o seguinte comando no terminal dentro do diretório do projeto:

python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
````

## 📦 Instalando as Dependências

Antes de rodar o projeto, é necessário instalar todas as bibliotecas utilizadas no backend e no frontend(npm install).

### 🔹 Backend (Python + Flask)

Certifique-se de que o ambiente virtual esteja ativado antes de instalar as dependências.

```bash
pip install flask mysql-connector-python pandas beautifulsoup4 requests flask-cors
````

### Criar o Banco de Dados MySQL

Acesse o MySQL
```bash
mysql -u root -p
````

## Crie o bando de dados e tabelas

```bash
Create DATABASE test_db;
USE test_db;

CREATE TABLE operadoras_plano_saude (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2)
);

CREATE TABLE despesas_operadoras (
    reg_ans INT,
    descricao VARCHAR(255),
    vl_saldo_final DECIMAL(18,2),
    data DATE
);
````

### Configurar o Backend

```bash
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sua_senha',
    'database': 'test_db'
}
````

## 📥 **Populando o Banco de Dados**

Para preencher a base de dados com informações reais, utilize o script importar_csv.py.

### **Sobre o script**
O script importar_csv.py lê os arquivos .csv que contêm os dados de despesas das operadoras e insere essas informações no banco de dados MySQL. Ele:

- Abre cada arquivo CSV localizado no diretório banco_de_dados/
- Faz a conversão de valores para o formato correto (ex: substituindo vírgulas por pontos em valores monetários)
- Insere os dados na tabela despesas_operadoras

### **Como executar**

 **Configure o arquivo .env** na raiz do projeto com as credenciais do banco:
   
env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=sua_senha
   DB_NAME=test_db

   ### Execute o script de importação:

   ```bash
    python importar_csv.py
   ```


### Rodando o Backend

```bash
python app.py
````
