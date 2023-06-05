import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
c = conn.cursor()
c.execute("SELECT * FROM pet;")
pet_table = c.fetchall()
for data in pet_table:
    print(data)
c.close()
conn.close()