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

# create table vehiculos
# try:
#     cursor.execute('create table vehiculos (id_vehiculo SERIAL PRIMARY KEY, marca varchar(30) not null, modelo varchar(30) not null, propietario varchar(30) not null);')
#     conexion.commit()
# except Exception as err:
#     print("No se pudo crear la tabla", err);
# else:
#     print("Tabla creada de manera correcta")


# insert into vehiculos a single line of values
# try: 
#     cursor.execute("INSERT INTO vehiculos VALUES (2, 'Toyota', 'Corolla Hibrido', 'Purdy Motors')")
#     conexion.commit()
# except Exception as err:
#     print("Error al insertar datos", err)
# else:
#     print("Datos insertados correctamente")


# insert into vehicule an array o items
# vehiculosNuevos = [
#     (1, 'Ford', 'F-150', 'Concesionaria A'),
#     (2, 'Chevrolet', 'Camaro', 'Concesionaria B'),
#     (3, 'Toyota', 'Corolla', 'Concesionaria C'),
#     (4, 'Honda', 'Civic', 'Concesionaria D'),
#     (5, 'Hyundai', 'Elantra', 'Concesionaria E'),
#     (6, 'Volkswagen', 'Jetta', 'Concesionaria F'),
#     (7, 'Nissan', 'Altima', 'Concesionaria G'),
#     (8, 'BMW', 'X5', 'Concesionaria H'),
#     (9, 'Mercedes-Benz', 'C-Class', 'Concesionaria I'),
#     (10, 'Audi', 'A4', 'Concesionaria J'),
#     (11, 'Lexus', 'RX', 'Concesionaria K'),
#     (12, 'Mazda', 'CX-5', 'Concesionaria L'),
#     (13, 'Kia', 'Soul', 'Concesionaria M'),
#     (14, 'Subaru', 'Impreza', 'Concesionaria N'),
#     (15, 'Jeep', 'Wrangler', 'Concesionaria O'),
#     (16, 'Dodge', 'Challenger', 'Concesionaria P'),
#     (17, 'Ram', '1500', 'Concesionaria Q'),
#     (18, 'GMC', 'Sierra', 'Concesionaria R'),
#     (19, 'Ford', 'Mustang', 'Concesionaria S'),
#     (20, 'Chevrolet', 'Equinox', 'Concesionaria T'),
#     (21, 'Toyota', 'Tundra', 'Concesionaria U'),
#     (22, 'Honda', 'CR-V', 'Concesionaria V'),
#     (23, 'Hyundai', 'Santa Fe', 'Concesionaria W'),
#     (24, 'Volkswagen', 'Golf', 'Concesionaria X'),
#     (25, 'Nissan', 'Rogue', 'Concesionaria Y'),
#     (26, 'BMW', 'M3', 'Concesionaria Z'),
#     (27, 'Mercedes-Benz', 'E-Class', 'Concesionaria A1'),
#     (28, 'Audi', 'Q5', 'Concesionaria B1'),
#     (29, 'Lexus', 'LS', 'Concesionaria C1'),
#     (30, 'Mazda', 'MX-5', 'Concesionaria D1'),
# ]


# try: 
#     cursor.executemany('INSERT INTO vehiculos (id_vehiculo, marca, modelo, propietario) VALUES (%s, %s, %s, %s)', vehiculosNuevos)
#     conexion.commit()
# except Exception as err:
#     print("Error al insertar datos", err)
# else:
#     print("Datos insertados correctamente")


# select all vehicles from vehiculos table
# try:
#     cursor.execute('select * from vehiculos')
#     consulta = cursor.fetchall()
# except Exception as err: 
#     print("No se pudo consultar", err)
# else:
#     print(consulta)


# add column to table vehiculos
# agregarPrimaryKey = 'ALTER TABLE vehiculos ADD COLUMN id_unico SERIAL PRIMARY KEY'
# try:
#     cursor.execute(agregarPrimaryKey)
#     conexion.commit()
# except Exception as err:
#     print("No se pudo agregar la tabla", err)
# else:
#     print("Columna agregada correctamente")


# select all from vehiculos where id =
# try:
#     cursor.execute('SELECT * from vehiculos where id_unico = 2')
#     consultarId = cursor.fetchall()
# except Exception as err:
#     print("No se pudo consultar", err)
# else:
#     print(consultarId)


# delete table vehiculos
# eliminarVhiculos = 'DROP TABLE vehiculos'
# try:
#     cursor.execute(eliminarVhiculos)
#     conexion.commit()
# except Exception as err:
#     print("No se pudo eliminar la tabla", err)
# else:
#     print("Tabla eliminada correctamente")


# # select all vehicles ordered by Descendant
# orderVehiculosByDesc = 'SELECT * FROM vehiculos ORDER BY marca DESC'
# try:
#     cursor.execute(orderVehiculosByDesc)
#     consulta = cursor.fetchall()
# except Exception as err:
#     print('No se pudo realizar la consulta')
# else:
#     print(consulta)


# select all vehicles ordered by Ascendant
# orderVehiculosByAsc = 'SELECT * FROM vehiculos ORDER BY marca ASC'
# try:
#     cursor.execute(orderVehiculosByAsc)
#     consulta = cursor.fetchall()
# except Exception as err:
#     print('No se pudo realizar la consulta')
# else:
#     print(consulta)


# export all vehiculos to CSV report
# try:
#     cursor.execute('select * from vehiculos')
#     consulta = cursor.fetchall()
#     csv_file = "vehiculos.csv"
#     with open(csv_file, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['id', 'marca', 'modelo', 'concecionario'])
#         for vehiculo in consulta:
#             writer.writerow(vehiculo)
#         print("datos exportados a CSV exitosamente")
# except Exception as err: 
#     print("No se pudo consultar", err)

# obtain vehiculos by dealer
vehiculosByDealer = 'SELECT * FROM vehiculos ORDER BY concecionario ASC'
try:
    cursor.execute(vehiculosByDealer)
    consulta = cursor.fetchall()
    csv_file = "vehiculosByDealer.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'marca', 'modelo', 'concecionario'])
        for vehiculo in consulta:
            writer.writerow(vehiculo)
        print("datos exportados a CSV exitosamente")
except Exception as err:
    print('No se pudo realizar la consulta')

conexion.close()
