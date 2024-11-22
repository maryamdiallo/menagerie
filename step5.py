import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boubacar@2013"
)

cursor = connection.cursor()

# Create the menagerie database
cursor.execute("CREATE DATABASE menagerie")
print("Database 'menagerie' created.")

cursor.close()
connection.close()
