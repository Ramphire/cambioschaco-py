import oracledb
import json
import os

def dbtransaction(body):

    if body is not None:

        # Parámetros para la conexión con la base de datos
        # Se definen en "Variables de Entorno" del S.O. compatible
        dbparam1 = os.environ.get("ORA_PARAM1")
        dbparam2 = os.environ.get("ORA_PARAM2")
        dbparam3 = os.environ.get("ORA_PARAM3")
        
        if dbparam1 is not None and dbparam2 is not None and dbparam3 is not None:
            with oracledb.connect(user=dbparam1, password=dbparam2, dsn=dbparam3) as connection:
                with connection.cursor() as cursor: # Para las conexiones con drivers antiguos usar previamente: " oracledb.init_oracle_client "
                    out_val = cursor.var(str)
                    #clob_json = json.dumps(body, cls=DecimalEncoder)
                    clob_json = json.dumps(body)
                    print("calling procedure... ")
                    print("json : ", clob_json)
                    try:
                        # Llama a un procedimiento para capturar el body del request. 
                        # En este caso la DB se encargaría de leer el JSON
                        cursor.execute('BEGIN WSP_TIPOS_CAMBIOS_CAMBIOSCHACO(:1, :2); END;', [clob_json, out_val])
                        print("result: ", out_val)
                    except:
                        print("Error al ejecutar el procedimiento.")
        else:
            print("Parámetros para la conexión nulos. Verificar en las variables de entorno ORA_PARAM1, ORA_PARAM2, ORA_PARAM3.")
    else:
        print("Nada que hacer, respuesta nula. ")