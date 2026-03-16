from fastapi import FastAPI
from src.calculator import add, subtract, multiply, divide

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Calculator API is running"}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": add(a, b)}


@app.get("/subtract")
def subtract_numbers(a: int, b: int):
    return {"result": subtract(a, b)}


@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result": multiply(a, b)}


@app.get("/divide")
def divide_numbers(a: int, b: int):
    return {"result": divide(a, b)}
