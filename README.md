# ETL Pipeline with Python, PostgreSQL, and dbt

A modern, lightweight ETL pipeline that extracts data from a public API, loads it into a PostgreSQL database, and transforms it using dbt. Includes automated data testing.

## 🛠 Stack

- **Python** — extraction and loading
- **PostgreSQL (Docker)** — data warehouse
- **dbt** — transformations and testing
- **GitHub** — version control

## 📁 Project Structure

    etl_pipeline_project/
    ├── etl/ # Python ETL scripts
    ├── dbt/etl_dbt/ # dbt project
    ├── orchestration/ # (future: Prefect flows)
    ├── ci_cd/ # (future: GitHub Actions)
    ├── requirements.txt
    └── README.md


## 🚀 How to Run

1. Clone repo and create virtual environment
2. Install dependencies:
```pip install -r requirements.txt```
3. Start PostgreSQL:
```docker run --name etl-postgres -e POSTGRES_PASSWORD=etlpass -p 5433:5432 -d postgres```
4. Run the pipeline:
```python etl/extract_and_load.py```
5. Transform and test with dbt:
```
cd dbt/etl_dbt
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

**Shaheryar**  
_MSc Data Science & Engineering, Uppsala University_

