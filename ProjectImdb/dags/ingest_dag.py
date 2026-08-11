from __future__ import annotations

from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from cosmos import (
    DbtTaskGroup,
    ExecutionConfig,
    ProfileConfig,
    ProjectConfig,
    RenderConfig,
)
from cosmos.constants import TestBehavior
from imdb_ingest import load_imdb_data
DBT_PROJECT_PATH = Path("/opt/airflow/dbt_project")
DBT_PROFILES_YML = DBT_PROJECT_PATH / "profiles.yml"

project_config = ProjectConfig(
    dbt_project_path=DBT_PROJECT_PATH,
)

profile_config = ProfileConfig(
    profile_name="ProjectImdb",
    target_name="dev",
    profiles_yml_filepath=DBT_PROFILES_YML,
)

execution_config = ExecutionConfig(
    dbt_executable_path="dbt",
)

# Emit a separate Airflow task for tests after each model
render_config = RenderConfig(
    test_behavior=TestBehavior.AFTER_EACH,
    exclude=["example"],
)
default_args = {
    "owner": "IMDb",
    "depends_on_past": False,
    "retries": 1,
}
with DAG(
dag_id="ingest_dag",
description="IMDb: parquet → DuckDB bronze → dbt staging/marts",
default_args=default_args,
start_date=datetime(2026, 7, 1),
schedule=None,
catchup=False,
max_active_tasks=1,
tags=["IMDb", "duckdb", "dbt"],
doc_md="""
### IMDb pipeline

1. **load_IMDb_data** — parquet → `bronze.IMDb`
2. **validate_bronze** — fail fast if Bronze is empty
3. **dbt_seed** — load `taxi_zone_lookup`
4. **dbt_run** — staging → intermediate → marts
5. **dbt_test** — schema + custom tests
""",
) as dag:
    start = EmptyOperator(task_id="start")

    load =PythonOperator(
    task_id="load_imdb_data",
    python_callable=load_imdb_data,
    )
    finish =EmptyOperator(task_id="finish")
    start>>load>>finish