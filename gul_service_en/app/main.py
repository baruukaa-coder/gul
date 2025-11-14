from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import os

app = FastAPI()

mongo_uri = os.environ.get("MONGO_URI")
db_name = os.environ.get("DB_NAME")

client = MongoClient(mongo_uri)
db = client[db_name]

@app.get("/health/db")
def health_db():
    try:
        db.list_collection_names()
        return {"status": "ok", "db": db_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
