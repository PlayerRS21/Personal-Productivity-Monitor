import mysql.connector
from mysql.connector import Error
import variables as v

cursor=""
conn=""
dbconnected=False

# Connecting DataBase
def connectDB():
    global cursor
    global conn
    global dbconnected
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
        cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,userName VARCHAR(50) NOT NULL UNIQUE,email VARCHAR(70) NOT NULL UNIQUE,password VARCHAR(100) NOT NULL,created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,last_login TIMESTAMP DEFAULT NULL)AUTO_INCREMENT=1000")
        # (id,username,email,password,created_on,last_login)
        
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INT AUTO_INCREMENT UNIQUE,taskName VARCHAR(100) NOT NULL,category INT NOT NULL,user_id INT NOT NULL)")
        # (id, taskName, category, user_id)
        
        cursor.execute("CREATE TABLE IF NOT EXISTS sessions (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL, task_id INT, created_at TIMESTAMP NOT NULL, ended_at TIMESTAMP, total_time INT, break_taken INT DEFAULT 0, status VARCHAR(20), CONSTRAINT foreign_id FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE)")
        # (id, user_id, task_id, created_at, ended_at, total_time, break_taken, status)
        
        cursor.execute("CREATE TABLE IF NOT EXISTS categories (category_id INT AUTO_INCREMENT PRIMARY KEY, category_name VARCHAR(100) NOT NULL UNIQUE, user_id INT NOT NULL)AUTO_INCREMENT=100")
        # (category_id, category_name, user_id)
        
        
        dbconnected=True
        return (True,conn,cursor)
    except mysql.connector.Error as e:
        print(f"Error connecting to Database: \n\n{e}")
        exit()

# Executing Commands
def DBExecute(querry,data:tuple|list):
            
    global dbconnected
    
    if not dbconnected:
        connectDB()
        
    try:
        cursor.execute(querry,data)
        return cursor.fetchall()
        
    except Error as e:
        print(e)
        exit()

# Adding User
def addUserEntry(data:tuple|list):

    global dbconnected
    if not dbconnected:
        connectDB()
        
    query="INSERT INTO users (userName,email,password) VALUES (%s,%s,%s)"
    try:
        cursor.execute(query,data)
        conn.commit()
        return {"status":True,"error":None}
        
    except Error as e:
        e=str(e)
        if "Duplicate entry" in e:
            if "userName" in e:
                # print("UserName Already in use")
                 return {"status":False,"error":"User Name Already in use"}
            elif "email" in e:
                # print("Email Already in use")
                return {"status":False,"error":"Email Already in use"}
        else:
            return {"status":False,"error":e}

# Saving Data
def DBSaveData(querry,data:tuple|list):
        
    global dbconnected
    if not dbconnected:
        connectDB()
        
    try:
        cursor.execute(querry,data)
        conn.commit()
        return {"status": True,"error":None}
        
    except Error as e:
        # print(e)
        return {"status": False,"error":e}

def getid():
    return cursor.lastrowid

if __name__=="__main__":
    connectDB()
