# 💰 Data Pipeline: Extração de Preço da Bitcoin com ETL em Python + Microsoft Azure

Este projeto faz parte de um workshop introdutório de Engenharia de Dados. O foco é desenvolver um pipeline ETL (Extract, Transform, Load) completo, utilizando Python e a API pública da Coinbase, com armazenamento local e possibilidade de expansão para nuvem (ex: Microsoft Azure) e visualização com dashboard interativo.


---

## 🎯 Objetivo

Criar um processo automatizado que:

- Consulta a **API da Coinbase** para obter o preço atual da Bitcoin.
- Processa e organiza esses dados.
- Armazena os resultados localmente (CSV) ou em banco de dados.
- Permite visualização futura através de dashboards.

---

## 📦 Estrutura do Projeto

data-pipeline-bitcoin/
├── main.py # Script principal de execução do ETL
├── database.db # (opcional) Banco de dados SQLite
├── bitcoin_prices.csv # Arquivo de saída com os preços coletados
├── dashboard.py # Script para visualização com Streamlit
├── requirements.txt # Dependências do projeto
└── README.md # Documentação


---

## ⚙️ Etapas do Pipeline

### 🔹 1. Extração (Extract)

- Utiliza a **API pública da Coinbase** para acessar o preço atual da Bitcoin em USD.
- Não requer autenticação.

### 🔹 2. Transformação (Transform)

- Seleciona as colunas relevantes: preço, horário da consulta e moeda.
- Estrutura os dados como tabela usando `pandas`.

### 🔹 3. Carga (Load)

- Salva os dados:
  - Em um arquivo `.csv` para análise local.
  - Ou em um banco SQLite com `sqlite3`.
  - Ou ainda com `tinydb` (NoSQL leve).

### 🔄 4. Automação

- Pode ser agendado para execução automática (com cron, Airflow ou scripts).
- Garante coleta contínua ao longo do tempo.

---

## 🧪 Exemplo de Dados

| Data/Hora           | Preço (USD) | Moeda   |
|---------------------|-------------|---------|
| 2024-01-01 12:00:00 | 42,000.50   | Bitcoin |
| 2024-01-01 13:00:00 | 42,150.75   | Bitcoin |

---

## 🔧 Tecnologias e Bibliotecas

- **Python 3.12+**
- [`requests`](https://pypi.org/project/requests/) – consumo de API
- [`pandas`](https://pandas.pydata.org/) – estruturação dos dados
- [`sqlite3`] – banco de dados relacional local (opcional)
- [`tinydb`](https://tinydb.readthedocs.io/) – banco de dados NoSQL em JSON (opcional)
- [`sqlalchemy`](https://www.sqlalchemy.org/) – ORM para acesso a SQL
- [`psycopg2-binary`](https://pypi.org/project/psycopg2-binary/) – conexão com PostgreSQL
- [`streamlit`](https://streamlit.io/) – visualização de dados com dashboard
- `time`, `datetime` – manipulação de tempo

---

## ✅ Resultados Esperados

- Pipeline automatizado para coleta de dados da API da Coinbase.
- Armazenamento em CSV ou banco local.
- Capacidade de analisar e visualizar a evolução do preço da Bitcoin ao longo do tempo.

### 🔍 Possibilidades de Análise

- Tendências de preço por hora, dia ou mês.
- Picos de alta/baixa com alertas.
- Visualização em tempo real com dashboards Streamlit.

---

## 🛠️ Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/data-pipeline-bitcoin.git
cd data-pipeline-bitcoin

2. Instale as dependências
bash
Copy
Edit
pip install -r requirements.txt
3. Execute o script principal
bash
Copy
Edit
python main.py
4. Verifique os dados
O arquivo bitcoin_prices.csv será gerado com os dados coletados.

📊 Dashboard (Opcional)
Execute o Streamlit para visualizar os dados:

bash
Copy
Edit
streamlit run dashboard.py
