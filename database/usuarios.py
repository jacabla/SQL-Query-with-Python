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


# create table usuarios
# try:
#     cursor.execute('create table usuarios (id_usuario SERIAL PRIMARY KEY, nombre varchar(30) not null, apellido varchar(30) not null, edad smallint not null);')
#     conexion.commit()
# except Exception as err:
#     print("No se pudo crear la tabla", err);
# else:
#     print("Tabla creada de manera correcta")


# # create array with usuarios to bi inserted into usuarios table
# personas = [(1, 'Ana', 'Alpizar', 36), (2, 'Juan', 'Martinez', 28), (3, 'Carla', 'García', 42), (4, 'Diego', 'Ramírez', 19), (5, 'María', 'Fernández', 56),    (6, 'Luis', 'González', 31),    (7, 'Marta', 'Vargas', 24),    (8, 'Jorge', 'Hernández', 47),    (9, 'Sofía', 'Pérez', 39),    (10, 'Andrés', 'Díaz', 23),    (11, 'Alejandra', 'Torres', 30),    (12, 'Gabriel', 'Sánchez', 50),    (13, 'Fernanda', 'López', 27),    (14, 'Eduardo', 'Castillo', 41),    (15, 'Lucía', 'Ruiz', 18),    (16, 'José', 'Fuentes', 34),    (17, 'Paulina', 'Jiménez', 22),    (18, 'Roberto', 'Lara', 29),    (19, 'Amanda', 'Sosa', 37),    (20, 'Miguel', 'Paz', 48),    (21, 'Valeria', 'Rojas', 21),    (22, 'Mario', 'Cortés', 45),    (23, 'Camila', 'Álvarez', 26),    (24, 'Francisco', 'Gómez', 53),    (25, 'Isabel', 'Sandoval', 33),    (26, 'Ricardo', 'Espinoza', 40),    (27, 'Paola', 'Herrera', 25),    (28, 'Pablo', 'Navarro', 32),    (29, 'Renata', 'Salazar', 44),    (30, 'Pedro', 'Flores', 38)]


# # insert array personas into usuarios
# try: 
#     cursor.executemany('INSERT INTO usuarios (id_usuario, nombre, apellido, edad) VALUES (%s, %s, %s, %s)', personas)
#     conexion.commit()
# except Exception as err:
#     print("Error al insertar datos", err)
# else:
#     print("Datos insertados correctamente")


# # query database:
# # select all users from database
# try:
#     cursor.execute('select * from usuarios')
#     consulta = cursor.fetchall()
# except Exception as err: 
#     print("No se pudo consultar", err)
# else:
#     print(consulta)


# # select all users from database ordered by nombre Descendant
# SelectUsuariosByOrderDesc = 'SELECT * FROM usuarios ORDER BY nombre DESC'
# try:
#     cursor.execute(SelectUsuariosByOrderDesc)
#     consulta = cursor.fetchall()
# except Exception as err: 
#     print("No se pudo consultar", err)
# else:
#     print(consulta)


# # select all users from database ordered by nombre Ascendant
# SelectUsuariosByOrderAsc = 'SELECT * FROM usuarios ORDER BY nombre ASC'
# try:
#     cursor.execute(SelectUsuariosByOrderAsc)
#     consulta = cursor.fetchall()
# except Exception as err: 
#     print("No se pudo consultar", err)
# else:
#     print(consulta)


# # select all users from database by name
# SelectUsuariosByName = "SELECT * FROM usuarios WHERE nombre = 'Luis'"
# try:
#     cursor.execute(SelectUsuariosByName)
#     consulta = cursor.fetchall()
# except Exception as err: 
#     print("No se pudo consultar", err)
# else:
#     print(consulta)


# # delete table usuarios
# deleteUsuarios = 'DROP TABLE usuarios'
# try:
#     cursor.execute(deleteUsuarios)
#     conexion.commit()
# except Exception as err:
#     print("No se pudo eliminar la tabla", err)
# else:
#     print("Tabla eliminada correctamente")

# # delete user by ID
# eliminarUsuarioById = 'DELETE FROM usuarios WHERE id_usuario = 1'
# try:
#     cursor.execute(eliminarUsuarioById)
#     conexion.commit()
# except Exception as err:
#     print("No se pudo eliminar el usuario", err)
# else:
#     print("Usuario eliminado correctamente")

#  # select user by ID
# id_usuario = 31;

# selectUsuarioById = 'SELECT * FROM usuarios WHERE id_usuario = %s'
# try:
#     cursor.execute(selectUsuarioById, (id_usuario,))
#     consulta = cursor.fetchall()
#     conexion.commit()
# except Exception as err:
#     print("No se pudo consultar el usuario:", err)
# else:
#     print(consulta)


# # export all usuarios to CSV report
# try:
#     cursor.execute('select * from usuarios')
#     consulta = cursor.fetchall()
#     csv_file = "usuarios.csv"
#     with open(csv_file, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['id_usuario', 'nombre', 'apellido', 'edad'])
#         for usuario in consulta:
#             writer.writerow(usuario)
#         print("datos exportados a CSV exitosamente")
# except Exception as err: 
#     print("No se pudo consultar", err)

cursor.close()
conexion.close()
