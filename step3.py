import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013"
)

cursor = connection.cursor()
cursor.execute("SHOW DATABASES")

print("Databases:")
for db in cursor:
    print(db[0])

cursor.close()
connection.close()
