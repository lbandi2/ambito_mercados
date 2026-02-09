from typing import Dict
from fastapi import FastAPI

from app.query import fetch_data

app = FastAPI()


def riesgo_pais() -> Dict[str, str] | None:
    return fetch_data(path='/riesgopais/variacion-ultimo')

def dolar_blue() -> Dict[str, str] | None:
    return fetch_data(path='/dolar/informal/variacion')

def dolar_oficial() -> Dict[str, str] | None:
    return fetch_data(path='/dolarnacion/variacion')

@app.get("/riesgo_pais/")
async def _riesgo_pais():
    """
    Retrieve values for riesgo pais
    """
    return riesgo_pais()

@app.get("/dolar_blue/")
async def _dolar_blue():
    """
    Retrieve values for dolar blue
    """
    return dolar_blue()

@app.get("/dolar_oficial/")
async def _dolar_oficial():
    """
    Retrieve values for dolar oficial
    """
    return dolar_oficial()
