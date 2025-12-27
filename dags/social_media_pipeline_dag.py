from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.ingestion.twitter_ingest import fetch_tweets
from src.processing.clean_transform import clean_data
from src.analytics.metrics_analysis import analyze_metrics
from src.storage.db_loader import load_to_postgres

default_args = {
    "owner": "data-engineering",
    "retries": 1
}

with DAG(
    dag_id="social_media_metrics_pipeline",
    start_date=datetime(2024, 11, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args
) as dag:

    ingest = PythonOperator(
        task_id="fetch_twitter_data",
        python_callable=fetch_tweets
    )

    transform = PythonOperator(
        task_id="clean_transform_data",
        python_callable=clean_data
    )

    analyze = PythonOperator(
        task_id="analyze_social_metrics",
        python_callable=analyze_metrics
    )

    load = PythonOperator(
        task_id="load_data_postgres",
        python_callable=load_to_postgres
    )

    ingest >> transform >> analyze >> load
