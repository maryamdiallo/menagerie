import mysql.connector

# Initialize the connection variable
connection = None

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your username
        password="Boubacar@2013"  # Replace with your password
    )
    if connection.is_connected():
        print("Connection successful")
except mysql.connector.Error as err:
    print(f"Connection error: {err}")
finally:
    if connection and connection.is_connected():
        connection.close()
        print("Connection closed")
