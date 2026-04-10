from airflow import DAG
from aiflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="run_dbt_pipeline",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:
    
    run_dbt = BashOperator(
        task_id="dbt_build",
        bash_command="cd /opt/airflow/dbt-repo && dbt build"
    )