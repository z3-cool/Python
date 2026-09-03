import mysql.connector
persona_db = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'admin',
    database ='persona_db'
)
cursor = persona_db.cursor()
sentencia_sql ='INSERT INTO personas2(nombre,apellido,edad) VALUES(%s,%s,%s)'
valores =('joaquin','ramos',77)
cursor.execute(sentencia_sql, valores)
persona_db.commit()
print(f'se ha insertado un nuevo registro: {valores}')
cursor.close()
persona_db.close()