import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013",
    database="menagerie"
)

cursor = connection.cursor()

# Count pets for each owner
cursor.execute("SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner")

print("Number of pets each owner has:")
for record in cursor:
    print(record)

cursor.close()
connection.close()
