from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

with DAG(dag_id='trigger_airbyte_job_example',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily',
         start_date=days_ago(1)
    ) as dag:

    money_to_json = AirbyteTriggerSyncOperator(
        task_id='airbyte_money_json_example',
        airbyte_conn_id='airbyte_conn_example',
        connection_id='1e3b5a72-7bfd-4808-a13c-204505490110',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )