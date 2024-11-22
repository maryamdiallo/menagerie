import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013"
)

cursor = connection.cursor()

# Drop the menagerie database if it exists
cursor.execute("DROP DATABASE IF EXISTS menagerie")
print("Database 'menagerie' dropped (if it existed).")

cursor.close()
connection.close()
