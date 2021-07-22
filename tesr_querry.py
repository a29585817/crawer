import mysql.connector

cnx = mysql.connector.connect(user='root', host = "127.0.0.1", password='a0937004538', database = "pchome")
cursor = cnx.cursor(dictionary=True)

query = ("SELECT * FROM product "
         "WHERE name LIKE '%ASUS%'")


cursor.execute(query)

for row in cursor:
  print(row)
  print(row["name"])

cursor.close()
cnx.close()