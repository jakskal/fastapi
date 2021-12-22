from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/luas-persegi/{sisi}")
def luas_persegi(sisi: int):
    luas = hitung_luas_persegi(sisi)
    return {"sisi persegi": sisi, "luas":luas}

@app.get("/keliling-persegi/{sisi}")
def keliling_persegi(sisi: int):
    luas = hitung_keliling_persegi(sisi)
    return {"sisi persegi": sisi, "luas":luas}

@app.get("/print-input/{input}")
def print_input(input):
    input_print = printinput(input)
    return {"input": input_print}

def hitung_luas_persegi(sisi: int)->int:
    if sisi < 0 :
        sisi = -1 * sisi
    return sisi*sisi

def printinput(input):
    return input

def hitung_keliling_persegi(sisi: int)->int:
    if sisi < 0 :
        sisi = -1 * sisi
    return 4*sisi
