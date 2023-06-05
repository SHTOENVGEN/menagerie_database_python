import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
c = conn.cursor()
c.execute('SELECT * FROM pet WHERE species = "dog" AND sex = "f"')
pet_table = c.fetchall()
for f_dog in pet_table:
    print(f_dog)
c.close()
conn.close()