from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators import MySqlOperator

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pytz import timezone
from redis import Redis

import json
import time
import requests
import re

schedule_interval='@once'

start_date = datetime(2020, 10, 28)
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "wait_for_downstream": True,
    "start_date": start_date,
    "retries": 1,
    "retry_delay": timedelta(seconds=1),
    "provide_context": True
}

def get(**kwargs):
    ti = kwargs['ti']
    base_api='https://disease.sh/v3/covid-19/nyt/usa?lastdays=30'
    data = requests.get(url = base_api).json()
    return data

def save(**kwargs):
    ti = kwargs['task_instance']
    data = ti.xcom_pull(task_ids='get_usa_COVID_daily')
    headers = {'Content-Type': 'application/json'}
    api = 'http://backend:8000/rad/usa_daily'
    print(requests.post(api, data=json.dumps(data),
                    headers=headers).json())


# scheduler DAGs
dag = DAG("USA-COVID-daily",
          default_args=default_args,
          schedule_interval=schedule_interval)

t1 = PythonOperator(task_id='get_usa_COVID_daily',
                    python_callable=get,
                    dag=dag)

t2 = PythonOperator(task_id='save_usa_COVIDdaily',
                    python_callable=save,
                    dag=dag)

t1 >> t2
