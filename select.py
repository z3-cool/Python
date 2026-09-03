# hacemos la conexiones con python a la bd 
# de mysql
# agregamos unos registros y demas por mysql 
# luego hacemos la conexion
#ahora vamos a crear otro archivo para 
# eliminar , actualizar e insertar la bd 

import mysql.connector
persona_db = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'admin',
    database ='persona_db'
)
cursor = persona_db.cursor()
cursor.execute('SELECT * FROM personas2')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)
cursor.close()
persona_db.close()