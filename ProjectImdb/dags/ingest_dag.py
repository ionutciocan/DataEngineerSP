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
from scripts.imdb_ingest import load_imdb_data

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

render_config = RenderConfig(
    test_behavior=TestBehavior.AFTER_EACH,
)

default_args = {
    "owner": "IMDb",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
        dag_id="imdb_end_to_end_pipeline",
        description="IMDb: parquet → DuckDB bronze → dbt staging/marts",
        default_args=default_args,
        start_date=datetime(2026, 7, 1),
        schedule_interval="@weekly",
        catchup=False,
        max_active_tasks=1,
        tags=["IMDb", "duckdb", "dbt"],
        doc_md="""
    ### IMDb Data Pipeline

    1. **load_imdb_data**: Extraction & Loading into DuckDB
    2. **run_dbt_snapshots**: Tracks Slowly Changing Dimensions (SCD Type 2)
    3. **transform_and_test**: dbt staging -> intermediate -> marts -> validation tests
    """,
) as dag:
    start = EmptyOperator(task_id="start")

    load = PythonOperator(
        task_id="load_imdb_data",
        python_callable=load_imdb_data,
    )

    run_snapshots = BashOperator(
        task_id="run_dbt_snapshots",
        bash_command=f"dbt snapshot --project-dir {DBT_PROJECT_PATH} --profiles-dir {DBT_PROJECT_PATH}",
    )

    dbt_transform_and_test = DbtTaskGroup(
        group_id="transform_and_test",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
        render_config=render_config,
    )

    finish = EmptyOperator(task_id="finish")

    start >> load >> run_snapshots >> dbt_transform_and_test >> finish