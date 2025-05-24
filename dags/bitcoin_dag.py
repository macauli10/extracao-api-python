from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

def rodar_script():
    subprocess.run(["python3", "/opt/airflow/scripts/main.py"])

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 24),
    'retries': 1,
    'retry_delay': timedelta(seconds=15),
}

with DAG(
    'coleta_bitcoin_csv',
    default_args=default_args,
    schedule_interval='*/1 * * * *',  
    catchup=False
) as dag:
    
    tarefa_rodar_script = PythonOperator(
        task_id='executar_script_bitcoin',
        python_callable=rodar_script
    )
