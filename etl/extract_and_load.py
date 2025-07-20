import requests
import pandas as pd
from sqlalchemy import create_engine, text


# --- CONFIG ---
DB_URI = "postgresql://postgres:etlpass@localhost:5433/etl_db"

API_URL = "https://randomuser.me/api/?results=10"

# --- EXTRACT ---
def extract():
    res = requests.get(API_URL)
    data = res.json()['results']
    
    df = pd.DataFrame([{
        "name": f"{x['name']['first']} {x['name']['last']}",
        "email": x['email'],
        "city": x['location']['city']
    } for x in data])
    
    return df

# --- LOAD ---
def load(df):
    engine = create_engine(DB_URI)
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))  # ✅ Add this line
    df.to_sql("fake_users", engine, schema="raw", if_exists="append", index=False)
    print("✅ Data loaded into raw.fake_users")


if __name__ == "__main__":
    df = extract()
    print(df.head())
    load(df)
