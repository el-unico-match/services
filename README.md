# services

> 
> __Funcionalidades actuales__
> * Alta de Api Key
> * Cambio del estado de un Api Key: 'enabled', 'disabled', 'blocked'
> * Eliminación de una Api Key
> * Envío de whitelist ante un cambio en las Api Keys
> * Estado del servicio
> * Visualización de logs
> * Obtención de tipos de Servicios
> * Obteneción del código de estado de los servicios asociados
>
> __Cobertura de código__
> * [![Coverage Status](https://coveralls.io/repos/github/el-unico-match/services/badge.svg?branch=coveral-integration)](https://coveralls.io/github/el-unico-match/services?branch=coveral-integration)
>
> <br/>

# Instrucciones

### Para ejecutar la aplicación local

##### Base de Datos
Instalar Docker y luego descargar el contenedor de la base de datos mongodb:
```bash
  docker pull mongo
```

Iniciar el contenedor de docker mediante la siguiente instrucción (puerto 5003 y contraseña asd123!)
```bash
  docker run --name services-database-mongodb -p 5003:27017  -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=asd123! mongo
```

##### Código

Descargar código en el actual repositorio
```bash
  git clone git@github.com:el-unico-match/services.git
```

##### Crear venv en MacOS
```bash
  mkdir .venv
  python3 -m venv .venv
  source .venv/bin/activate
```

##### Instalar los paquetes
```bash
  pip install -r requirements.txt
```

##### Visual Code

En el archivo **launch.config** de Visual Code agregar las siguientes líneas

```json
{   
    "name": "Services",
    "type": "debugpy",
    "request": "launch",
    "module": "uvicorn",
    "justMyCode": true,
    "args": [
        "services:app",
        "--reload",
        "--port",
        "4003",
        "--host",
        "0.0.0.0"
    ],
    "jinja": true,
    "cwd": "${workspaceFolder}/services/src",
    "python": "${workspaceFolder}/services/.venv/bin/python",
    "preLaunchTask": "Starts Services Container Database"
}
```

En el archivo **tasks.json** de Visual Code agregar la siguiente instrucción para levantar docker
```json
{
    "label": "Starts Services Container Database",
    "type": "shell",
    "command": "docker",
    "args": ["start", "services-database-mongodb"]
},
```

Crear el siguiente archivo **dev.env** y ubicarlo dentro de la carpeta match. 
```bash
    LOG_FILEPATH=log.txt
    LOG_LEVEL=10
    APP_SITE=localhost:4003
    APP_VERSION= #número de commit
    jwt_private_key= #key para generar jwt
    db_url=mongodb://admin:asd123!@localhost:5003 #ruta a la base de datos de mongo
    apikey_value= #keyPorDefecto 
    apikey_whitelist= #WhiteList pr defecto
    apikey_activate_endpoint= #Endpoint para recibir requests para activar apikey
```

*Nota 1*: la whitelist es un conjunto de JWT separados por espacio.
*Nota 2*: el activate endpoint es el baseUrl de la actual aplicación y luego agrega /api/v1/services/
	 
##### Para acceder a la documentación con swagger: 
  1) Abrir el navegador
  2) Escribir en la barra de direcciones: http://localhost:4003/api-docs 

##### Probar cobertura de código
Para probar la cobertura se puede ejecutar desde un .venv:
```bash
  pytest --cov=. 
```  
