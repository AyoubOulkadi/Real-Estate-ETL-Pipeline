import os
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from src.data_collection.main import scraper
from preprocessing_data import preprocessing

default_args = {
    'owner': 'Ayoub_oulkadi',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 8),
    'email': [os.getenv("email")],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Instantiate a DAG object
real_estate_dag = DAG('real_estate_dag',
                      default_args=default_args,
                      description='real_estate',
                      schedule_interval='@daily_data',
                      catchup=False
                      )
start_task = DummyOperator(task_id='start_task', dag=real_estate_dag)
scraper_task = PythonOperator(task_id='scraper_task', python_callable=scraper, dag=real_estate_dag)
processing_task = PythonOperator(task_id='processing_task', python_callable=preprocessing, dag=real_estate_dag)

# Set the order of execution of tasks.
start_task >> scraper_task >> processing_task
