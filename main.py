from typing import List
from fastapi import FastAPI, HTTPException, Depends
import config
from database import get_connection
from models import Car, Person
from db_helpers import fetch_all, fetch_one, insert_record, delete_record
from auth import basic_auth

conn = get_connection()
app = FastAPI()


@app.get("/")
def read_root():
    raise HTTPException(status_code=400, detail=str('Invalid path'))


@app.get("/users", response_model=List[Car], dependencies=[Depends(basic_auth)])
def getUsers():
    try:
        return fetch_all("SELECT * FROM cars;", ('model', 'year'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/users/{userId}")
def getUser(userId):
    try:
        car = fetch_one("SELECT * FROM cars WHERE model = %s;", (userId,))

        if car is None:
            raise HTTPException(status_code=404, detail="Car not found!!")

        return car
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/users")
def createUser(userData: Car):
    try:
        existing = fetch_one(
            "SELECT * FROM cars WHERE model = %s;", (userData.model,))

        if existing:
            raise HTTPException(
                status_code=400, detail="Car already exists")

        new_car = insert_record('cars', userData.model_dump())

        if not new_car:
            raise HTTPException(status_code=500, detail="Insert failed")

        return new_car
    except:
        raise


@app.delete("/users/{userId}")
def deleteUser(userId):
    try:
        deletedUser = delete_record("cars", "model = %s", (userId,))

        if not deletedUser:
            raise HTTPException(
                status_code=404, detail=f"User {userId} not deleted!!")

        return {
            "message": f"User {userId} deleted successfully!!"
        }
    except:
        conn.rollback()
        raise
