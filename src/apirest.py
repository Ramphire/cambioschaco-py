import requests
from conexion import dbtransaction

api_url = "https://www.cambioschaco.com.py/api/branch_office/1/exchange"

#def para el método GET
def consulta():
    respuesta = requests.get(api_url)
    status_code = respuesta.status_code
    print("Codigo de estado : ", status_code)
    if 200 <= status_code <= 299:
        clob_body = respuesta.json()
    else:
        print("No se pudo consultar la API. Status Code: ", status_code)
        clob_body = None

    return clob_body

def run():
    dbtransaction(consulta())