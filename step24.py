import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
c = conn.cursor()
c.execute("SELECT owner, COUNT(*) AS pets FROM pet GROUP BY owner;")
pet_table = c.fetchall()
column_title = c.description
print(f"('{column_title[0][0]}', '{column_title[1][0]}')")
for data in pet_table:
    print(data)
c.close()
conn.close()