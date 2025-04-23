from fastapi import FastAPI
from calculator import Calculadora
from pydantic import BaseModel

app = FastAPI()

class Entrada(BaseModel):
    n1 : float
    n2 : float

@app.post("/test")
def ola():
    return {"mensagem": "Olá!"}


@app.post("/soma")
def soma(dados: Entrada):
    n1 = dados.n1
    n2 = dados.n2
    calculadora = Calculadora(n1,n2)
    return {
        "valor_informado": n1,
        "segundo_valor": n2,
        "resultado": calculadora.soma()
    }

@app.post("/subt")
def subt(dados: Entrada):
    n1 = dados.n1
    n2 = dados.n2
    calculadora = Calculadora(n1,n2)
    return {
        "valor_informado": n1,
        "segundo_valor": n2,
        "resultado": calculadora.subt()
    }

@app.post("/mult")
def mult(dados: Entrada):
    n1 = dados.n1
    n2 = dados.n2
    calculadora = Calculadora(n1,n2)
    return {
        "valor_informado": n1,
        "segundo_valor": n2,
        "resultado": calculadora.mult()
    }

@app.post("/divi")
def divi(dados: Entrada):
    n1 = dados.n1
    n2 = dados.n2
    calculadora = Calculadora(n1,n2)
    return {
        "valor_informado": n1,
        "segundo_valor": n2,
        "resultado": calculadora.divi()
    }