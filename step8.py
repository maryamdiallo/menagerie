import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013",
    database="menagerie"
)

cursor = connection.cursor()

# Fetch female dogs
cursor.execute("SELECT * FROM pet WHERE species='dog' AND sex='female'")

print("Female dogs in the pet table:")
for record in cursor:
    print(record)

cursor.close()
connection.close()
