import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013",
    database="menagerie"
)

cursor = connection.cursor()

# Fetch all records
cursor.execute("SELECT * FROM pet")

print("Records in the pet table:")
for record in cursor:
    print(record)

cursor.close()
connection.close()
