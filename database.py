import mysql.connector
from mysql.connector import Error


# Connecting DataBase
def connectDB():
    global cursor
    global conn
    try:
        config = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "raja",
            "password": "",
            "database": ""
            }
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        # cursor.execute("DROP DATABASE productivityMonitor")
        cursor.execute("CREATE DATABASE IF NOT EXISTS productivityMonitor")
        cursor.execute("USE productivityMonitor")
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,userName VARCHAR(50) NOT NULL UNIQUE,email VARCHAR(70) NOT NULL UNIQUE,password VARCHAR(100) NOT NULL,created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,last_login TIMESTAMP DEFAULT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INT AUTO_INCREMENT UNIQUE,taskName VARCHAR(100) NOT NULL,category VARCHAR(100) NOT NULL,created_by VARCHAR(50),created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,total_time TIMESTAMP NOT NULL);")
        print("Successfully connected to MariaDB server!")
        return (True,conn,cursor)
    except mysql.connector.Error as e:
        print(f"Error connecting to Database: {e}")

# Executing Commands
def dbExecute(querry,data:tuple|list):
    try:
        cursor.execute(querry,data)
        return cursor.fetchall()
    except Error as e:
        print(e)
