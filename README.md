# 🪙 ETL de Preço do Bitcoin com Airflow e Docker

Este projeto realiza a coleta periódica do preço do Bitcoin usando a API pública da Coinbase e armazena os dados em um arquivo CSV. A orquestração é feita com Apache Airflow, utilizando Docker Compose para garantir um ambiente reproduzível.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10
- Apache Airflow 2.8.1
- Docker e Docker Compose
- API pública da [Coinbase](https://api.coinbase.com)
- PostgreSQL (banco do Airflow)

---

## 📦 Estrutura do Projeto

ETLPython/
├── dags/
│ └── etl_bitcoin_dag.py # DAG do Airflow que executa a coleta
├── scripts/
│ └── main.py # Script Python que coleta o preço e salva no CSV
├── data/
│ └── bitcoin_prices.csv # Arquivo CSV onde os dados são armazenados
├── docker-compose.yml # Orquestração dos containers com Airflow e PostgreSQL
├── requirements.txt # Bibliotecas necessárias (opcional)
└── README.md


---

## 📥 Pré-requisitos

- Docker e Docker Compose instalados
- Porta `8080` livre (para acessar o Airflow)
- Recomendado: usar um ambiente virtual para desenvolvimento local (opcional)

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ETLPython.git
cd ETLPython

2. Suba os containers com Docker Compose
bash
Copy
Edit
docker-compose up -d
3. Inicialize o banco de dados do Airflow
Este comando é necessário apenas na primeira vez:

bash
Copy
Edit
docker-compose run airflow-webserver airflow db init
4. Acesse o Airflow
Abra o navegador:

arduino
Copy
Edit
http://localhost:8080
Usuário padrão: airflow
Senha padrão: airflow

⚠️ Você pode criar um usuário com docker exec caso queira personalizar.

📅 Sobre a DAG
O agendamento está configurado para executar a cada 30 segundos, coletando o preço do Bitcoin e salvando no CSV (/opt/airflow/data/bitcoin_prices.csv).

Exemplo de dado salvo:
csv
Copy
Edit
timestamp,price_usd
2025-05-24 14:47:03,69123.45
🧠 Observação sobre memória
O script main.py também monitora o pico de uso de memória durante a execução usando o módulo tracemalloc do Python, exibindo o valor em MB no console.

🐳 Docker Compose Overview
Seu docker-compose.yml está configurado com:

postgres: Banco de dados para o Airflow

airflow-webserver: Interface web

airflow-scheduler: Agendamento de tarefas

Montagens de volumes para dags, scripts, e data

✍️ Autor
Macauli 👨‍💻
Projeto pessoal para aprender orquestração de ETLs com Airflow e Docker.

