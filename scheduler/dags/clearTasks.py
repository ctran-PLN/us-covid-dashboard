from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta

schedule_interval='@once'

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 2, 10),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    'provide_context': True
}
dag_id = 'USA-COVID-daily'
query1 = "delete from job where dag_id = '%s';" % dag_id
query2 = "delete from log where dag_id = '%s';" % dag_id
query3 = "delete from task_instance where dag_id = '%s';" % dag_id
query4 = "delete from sla_miss where dag_id = '%s';" % dag_id
query5 = "delete from dag_run where dag_id = '%s';" % dag_id
query6 = "delete from xcom where dag_id='%s';" % dag_id

dag = DAG("houseKeeping",
          default_args=default_args,
          schedule_interval=schedule_interval)
t1 = PostgresOperator(
      task_id='delete-job',
      postgres_conn_id='postgres_default',
      sql=query1,
      dag=dag)
t2 = PostgresOperator(
      task_id='delete-log',
      postgres_conn_id='postgres_default',
      sql=query2,
      dag=dag)
t3 = PostgresOperator(
      task_id='delete-task_instance',
      postgres_conn_id='postgres_default',
      sql=query3,
      dag=dag)
t4 = PostgresOperator(
      task_id='delete-sla_miss',
      postgres_conn_id='postgres_default',
      sql=query4,
      dag=dag)
t5 = PostgresOperator(
      task_id='delete-dag_run',
      postgres_conn_id='postgres_default',
      sql=query5,
      dag=dag)
t6 = PostgresOperator(
      task_id='delete-xcom',
      postgres_conn_id='postgres_default',
      sql=query6,
      dag=dag)
t1 >> t2 >> t3 >> t4 >> t5 >> t6
