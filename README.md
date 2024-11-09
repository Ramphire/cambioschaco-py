
## Cambios Chaco S.A. API

Estos scripts fueron desarrollados con la alternativa de evitar el uso de "APEX_WEB_SERVICES.MAKE_REST_REQUEST()" desde la base de datos.


#### API

```
  GET https://www.cambioschaco.com.py/api/branch_office/1/exchange
```

#### Observaciones:

- Script sencillo utilizado como puente de comunicación entre la api original y la base de datos de transacciones.
- Se debe crear un procedimiento de base de datos al cuál se llamará en el script para leer el JSON.
- Se deben parametrizar variables de entorno para las conexiones con la DB.


## Variables de Entorno (Environment Variables)

To run this project, you will need to add the following environment variables to your .env file

`ORA_PARAM1` : DB User

`ORA_PARAM2` : DB Password

`ORA_PARAM3` : DSN o HOST. Formato : " localhost/XEPDB1 "

