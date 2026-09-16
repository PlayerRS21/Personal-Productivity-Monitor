import mysql.connector
from mysql.connector import Error

class perpro:
    userVerified=False
    def __init__(self):
        try:
            config = {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "raja",
                "password": "",
                "database": ""
                }
            self.conn = mysql.connector.connect(**config)
            self.cursor = self.conn.cursor()
            self.cursor.execute("DROP DATABASE productivityMonitor")
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS productivityMonitor")
            self.cursor.execute("USE productivityMonitor")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,userName VARCHAR(50) NOT NULL UNIQUE,password VARCHAR(100) NOT NULL,created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INT AUTO_INCREMENT UNIQUE,taskName VARCHAR(100) NOT NULL,created_by VARCHAR(50) DEFAULT \"Testing\",created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
            print("Successfully connected to MariaDB server!")

        except mysql.connector.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
            
    def create_user(self):
        uName=input("Enter User Name:\n--> ")
        p=input("Enter Password or default will be 1234: ")
        querry="INSERT INTO users (userName,password) VALUES (%s,%s)"
        if p !="":
            data=(uName,p)
        elif p=="":
            data=(uName,1234)

        self.cursor.execute(querry,data)
        self.conn.commit()
        print(f"User \"{uName}\" is created.")

    def listUsers(self):
        self.cursor.execute("SELECT * FROM users;")
        print(self.cursor.fetchall())

    def loginUser(self):
        userName=input("Enter Your User Name: ")
        passw=input("Enter Your Password: ")
        try:
            self.cursor.execute("SELECT * FROM users")
            users=self.cursor.fetchall()
            print(users)
            print()
            if userName in users:
                if passw==users[userName][passw]:
                    userVerified = True
                    print(userVerified)
                    print(f"{userName}:{passw}")
            else:
                userVerified=False
                print(userVerified)
                print(f"{userName}:{passw}")

        except:
            print(f"User Unverified with credentials: uName={userName} password: {passw}")
       
z=input("Enter what you wany to do: ")
x=perpro()
if z=="cu":
    x.create_user()
elif z=="lu":
    x.listUsers()
