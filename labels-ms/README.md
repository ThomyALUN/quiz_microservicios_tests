Record Labels API

Este proyecto es una API para gestionar sellos discográficos, desarrollada con Flask y utilizando MySQL como base de datos.

Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

Python 3.9 o superior

MySQL

pip

Adicionalmente, asegúrate de tener configuradas las siguientes herramientas:

virtualenv para gestionar entornos virtuales de Python

Instalación y configuración

Clona el repositorio:

git clone <URL-del-repositorio>
cd <directorio-del-repositorio>

Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

Instala las dependencias:

pip install -r requirements.txt

Configura las variables de entorno:

Crea un archivo .env en el directorio principal del proyecto.

Define tu API Key y otros valores necesarios:

API_KEY=tu_api_key_aqui

Configura la base de datos:

Crea una base de datos en MySQL llamada record_labels_db:

CREATE DATABASE record_labels_db;

Asegúrate de configurar correctamente la URI de conexión en app.config['SQLALCHEMY_DATABASE_URI'] dentro del archivo principal (app.py).

Inicializa la base de datos:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Uso

Ejecuta la aplicación:

flask run

La aplicación estará disponible en http://127.0.0.1:5000/.

Rutas disponibles:

Generar sellos discográficos:

POST /api/generate_labels/

Encabezado requerido: LABELS-API-KEY

Cuerpo del JSON:

{
  "n": 10
}

Respuesta:

{
  "message": "10 record labels generated successfully!"
}

Obtener todos los sellos discográficos:

GET /api/record_labels/

Encabezado requerido: LABELS-API-KEY

Respuesta:

[
  {
    "id": 1,
    "name": "Label Name",
    "country": "Country"
  }
]

Estructura del proyecto

/
├── app.py               # Archivo principal
├── models.py            # Definiciones del modelo de base de datos
├── requirements.txt     # Dependencias del proyecto
├── migrations/          # Archivos de migración de la base de datos
├── utils.py             # Utilidades para el proyecto (e.g., generación de datos falsos)
└── .env                 # Variables de entorno

Dependencias

Las principales dependencias del proyecto son:

Flask

Flask-SQLAlchemy

Flask-Migrate

python-dotenv

pymysql

Puedes ver todas las dependencias en el archivo requirements.txt.

Notas adicionales

Migraciones: Las migraciones se gestionan con Flask-Migrate. Asegúrate de ejecutar flask db migrate y flask db upgrade cada vez que hagas cambios en los modelos.

Autenticación: La autenticación se realiza mediante un encabezado llamado LABELS-API-KEY. Asegúrate de incluir este encabezado en todas las solicitudes con el valor correcto definido en el archivo .env.
