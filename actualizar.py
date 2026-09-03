import mysql.connector
persona_db = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'admin',
    database ='persona_db'
)
cursor = persona_db.cursor()
sentencia_sql ='UPDATE personas2 SET nombre=%s, apellido=%s, edad=%s  WHERE id=%s'
valores =("victoria","flores",37,4)
cursor.execute(sentencia_sql, valores)
persona_db.commit()
print(f'se actualizo un registro')
cursor.close()
persona_db.close()