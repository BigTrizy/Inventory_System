from fastapi import FastAPI
from scripts.database import check_database


app = FastAPI()


@app.get("/")
def root():
    return {
        "status": "API is running"
    }


@app.get("/health")
def health():

    database_status = check_database()

    return {
        "api": "healthy",
        "database": "healthy" if database_status else "unavailable"
    }