import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013",
    database="menagerie"
)

cursor = connection.cursor()

# Fetch name and birth columns
cursor.execute("SELECT name, birth FROM pet")

print("Name and Birth columns:")
for record in cursor:
    print(record)

cursor.close()
connection.close()
