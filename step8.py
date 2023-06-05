import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20')
c = conn.cursor()
c.execute("DROP DATABASE IF EXISTS menagerie")
conn.commit()
c.close()
conn.close()