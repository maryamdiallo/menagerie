import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013",
    database="menagerie"
)

cursor = connection.cursor()

# Describe the pet table structure
cursor.execute("DESCRIBE pet")

print("Table Structure:")
for row in cursor:
    print(row)

cursor.close()
connection.close()
