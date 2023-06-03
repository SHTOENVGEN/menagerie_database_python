import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20')
c = conn.cursor()
c.execute("SHOW DATABASES")
db = c.fetchall()

for database in db:
    print(database[0])

c.close()
conn.close()