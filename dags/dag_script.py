from datetime import datetime , timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from extraction import run_extraction
from transformation import run_transformation
from loading import run_loading

my_args = {
    'owner' : 'airflow',
    'depends_on_past' : False ,
    'start_date' : datetime(2025, 1, 1),
    'email':'admin@gmail.com',
    'email_on_failure': False ,
    'email_on_retry': False ,
    'retries' : 1 ,
    'retries_delay' : timedelta(minutes=1)
    
}

dags = DAG(
    'zipco_foods_pipeline',
    default_args = my_args ,
    description = 'This represent zipco foods data management pipeline'

)

Extraction = PythonOperator(
    task_id = 'extraction_layer' ,
    python_callable = run_extraction ,
    dag = dags
)

Transformation = PythonOperator(
    task_id = 'transformation_layer' ,
    python_callable = run_transformation ,
    dag = dags
)

Loading = PythonOperator(
    task_id = 'loading_layer' ,
    python_callable = run_loading ,
    dag = dags
)

Extraction >> Transformation >> Loading