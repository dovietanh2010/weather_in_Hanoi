from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Thêm đường dẫn của `scripts/` vào sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))

# Import các module từ scripts/
from extract import extract
from transform import transform
from load import load

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('weather_etl', default_args=default_args, schedule ='* * * * *', catchup=False) as dag:
    task_extract = PythonOperator(task_id='extract_data', python_callable=extract)
    task_transform = PythonOperator(task_id='transform_data', python_callable=transform)
    task_load = PythonOperator(task_id='load_data', python_callable=load)

    task_extract >> task_transform >> task_load
