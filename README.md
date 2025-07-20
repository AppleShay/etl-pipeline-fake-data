# ETL Pipeline with Python, PostgreSQL, and dbt

A modern, lightweight ETL pipeline that extracts data from a public API, loads it into a PostgreSQL database, and transforms it using dbt. Includes automated data testing.

## 🛠 Stack

- Python 3.10
- PostgreSQL
- pandas, SQLAlchemy, Faker
- dbt for modeling and testin
- GitHub Actions for CI/CD

## 📁 Project Structure

    .
    ├── etl/ # Python scripts for extraction and loading
    │ └── extract_and_load.py
    ├── dbt/
    │ └── etl_dbt/ # dbt project for transformations & testing
    │ ├── models/
    │ │ └── staging/
    │ │ ├── stg_fake_users.sql
    │ │ └── schema.yml
    │ ├── dbt_project.yml
    │ └── profiles.yml # Injected during CI
    ├── requirements.txt
    └── .github/workflows/
    └── ci.yml # GitHub Actions workflow file

## 🔁 Pipeline Overview

### 1. **Extract & Load (Python)**
- Uses [`Faker`](https://faker.readthedocs.io/en/master/) to generate fake user data.
- Loads data into a PostgreSQL database (`raw.fake_users`).

### 2. **Transform (dbt)**
- Creates a staging model: `raw.stg_fake_users`.
- Applies business logic, formatting, or renaming as needed.

### 3. **Test (dbt tests)**
- Ensures data quality using dbt's built-in tests:
  - `not_null`
  - `unique`

### 4. **CI/CD (GitHub Actions)**
- Runs on every `push` and `pull_request` to `main`.
- Automates:
  - Database spin-up
  - Python ETL job
  - dbt transformations and tests
  - Upload of logs as artifacts

---

## 🚀 Run It Locally

```bash
# Start Postgres (Docker recommended)
docker run --name etl-postgres -e POSTGRES_PASSWORD=etlpass -p 5433:5432 -d postgres

# Install dependencies
pip install -r requirements.txt
pip install dbt-postgres

# Run Python ETL
python etl/extract_and_load.py

# Run dbt
cd dbt/etl_dbt
dbt deps
dbt run
dbt test
```
---

## ✅ Features

- Pulls fake user data from `randomuser.me`
- Cleans and stages data with dbt
- Validates uniqueness and nulls
- Fully isolated in Docker + venv

---

## 📌 Author

Built with ❤️ by **Shaheryar (AppleShay)**

_MSc Data Science & Engineering, Uppsala University_

