from __future__ import print_function

import logging

from airflow.models import Variable

from bitcoinetl.build_load_dag import build_load_dag

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# When searching for DAGs, Airflow will only consider files where the string “airflow” and “DAG” both appear in the
# contents of the .py file.
DAG = build_load_dag(
    dag_id='litecoin_load_dag',
    output_bucket=Variable.get('litecoin_output_bucket'),
    destination_dataset_project_id=Variable.get('destination_dataset_project_id'),
    chain='litecoin',
    notification_emails=Variable.get('notification_emails', ''),
    schedule_interval='30 5 * * *'
)
