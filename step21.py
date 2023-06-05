import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
c = conn.cursor()
c.execute("SELECT name, birth FROM pet;")
pet_table = c.fetchall()
column_title = c.description
print(f"('{column_title[0][0]}', '{column_title[1][0]}')")
for column in pet_table:
    print(column)
c.close()
conn.close()