import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
c = conn.cursor()
c.execute("DESCRIBE pet;")
pet_table = c.fetchall()
for row in pet_table:
    print(row)
c.close()
conn.close()