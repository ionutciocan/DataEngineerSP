# IMDb Data Engineering Pipeline

## Overview
This repository contains an end-to-end data engineering pipeline built to extract, transform, and model IMDb dataset updates. The project utilizes **Apache Airflow** for orchestration, **DuckDB** as a local analytical data warehouse, and **dbt** (integrated via `astronomer-cosmos`) for data transformation and quality testing.

## Project Structure
- `dags/` - Contains the Airflow DAG (`ingest_dag.py`) that orchestrates the pipeline.
- `dbt_project/` - The dbt project containing staging, intermediate, and mart models, alongside custom data quality tests.
- `raw/` - Local data lake where downloaded `.parquet` files are staged (git-ignored).
- `docs/` - Contains the final project documentation and written report.

## Prerequisites
To run this project locally, ensure you have the following installed:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (must be running)
- [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) (for running Airflow locally)
- A SQL Client like [DBeaver](https://dbeaver.io/) (optional, for querying the results)

## How to Run (From a Clean Slate)
Follow these step-by-step instructions to reproduce the pipeline from a completely clean DuckDB environment:

### 1. Clean the Environment
Before starting, ensure you have a clean slate by deleting the existing DuckDB database file. 
Navigate to the root directory of the project and delete the `warehouse.duckdb` file (if it exists).

### 2. Start the Airflow Infrastructure
Open a terminal in the project's root directory and initialize the Astro Airflow environment:
```bash
astro dev start