import mysql.connector
persona_db = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'admin',
    database ='persona_db'
)
cursor = persona_db.cursor()
sentencia_sql = 'DELETE FROM personas2 WHERE id=%s'
valores=(5,)
cursor.execute(sentencia_sql,valores)
persona_db.commit()
print("se ha eliminado un registro")
cursor.close()
persona_db.close()