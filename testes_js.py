import sqlite3

conn = sqlite3.connect('signatures.db')
cursor = conn.cursor()

cursor.execute("""
DROP TABLE signatures;
""")

 #gravando no bd
conn.commit()



#cursor.execute("""
#SELECT * FROM signatures;
#""")

#cu = cursor.fetchall()

#for c in cu[0]:
#	print(c)


cursor.execute("""
CREATE TABLE signatures (
        assinamentos TEXT 
    
);
""")
conn.close()
