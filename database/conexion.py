import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Conexión a la base de datos
def conexion_db():
    try:
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        conexion = psycopg2.connect(database=database, user=user, password=password)
        return conexion
    except Exception as err:
        print('Error conectando a la base de datos:', err)
        return None
