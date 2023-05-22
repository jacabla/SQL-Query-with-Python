import csv
from conexion import conexion_db

conexion = conexion_db()
if conexion is None:
    exit(1)
cursor = conexion.cursor()

# conection to database
try:
    cursor.execute('select version()')
    version = cursor.fetchone()
    print("Versión de PostgreSQL:", version)
except Exception as err:
    print('Error conectando a la base de datos:', err)
    exit(1)

# Función para realizar un INNER JOIN entre las tablas usuarios y vehiculos y exportar a CSV
def usuariosVehiculos():
    try:
        cursor.execute("SELECT usuarios.nombre, vehiculos.marca FROM usuarios INNER JOIN vehiculos ON usuarios.id_usuario = vehiculos.id_usuario")
        resultados = cursor.fetchall()
        csv_file = "usuarioAndVehicule.csv"
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['nombre', 'vehiculo'])
            for resultado in resultados:
                print("Nombre del usuario:", resultado[0])
                print("Nombre del vehículo:", resultado[1])
                writer.writerow([resultado[0], resultado[1]])
                print("---")
            print("Datos exportados a CSV exitosamente")
    except Exception as err:
        print("Error al realizar el INNER JOIN:", err)

usuariosVehiculos()

cursor.close()
conexion.close()
