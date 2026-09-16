import mysql.connector
from mysql.connector import Error
import time
from datetime import datetime

class perpro:
    userVerified=False
    userName=""
    startTime=""
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
            #self.cursor.execute("DROP DATABASE productivityMonitor")
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS productivityMonitor")
            self.cursor.execute("USE productivityMonitor")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,userName VARCHAR(50) NOT NULL UNIQUE,password VARCHAR(100) NOT NULL,created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INT AUTO_INCREMENT UNIQUE,taskName VARCHAR(100) NOT NULL,category VARCHAR(100) NOT NULL DEFAULT \"Other\",created_by VARCHAR(50) DEFAULT \"Testing\",created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,total_time TIMESTAMP NOT NULL);")
            print("Successfully connected to MariaDB server!")

        except mysql.connector.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit()
    def addActivity(self):
        if self.userVerified == True:
            """
            task=input(f""User: {self.userName} Started at: {self.startTime}
Enter Category you are working on:
1. Python
2. DSA
3. SQL
4. C++
5. Projects
6. Linux
7. Other
--------------> "")"""
            tsk={1:"Python",2:"DSA",3:"SQL",4:"C++",5:"Projects",6:"Linux",7:"Other"}
            print(f"User:{self.userName}--------------Login at:{self.startTime}\nSelect Category: ")
            for key,value in tsk.items():
                print(f"{key}. {value}")
            print()
            i=int(input("--> "))
            sTime=time.perf_counter()
            #sTime=str(datetime.now())[10:]
            work=input("Enter Task Name: ")
            sTimeHum=str(time.strftime("%H:%M:%S",time.localtime(time.time())))
            print(f"Task Started at {sTimeHum}\nPress Ctrl + C to exit.")
            try:
                z= input("")
                e
            except:
                eTime=time.perf_counter()
                #eTime=str(datetime.now())[10:]
                querry="INSERT INTO tasks (taskName,category,created_by,created_on,total_time) VALUES (%s,%s,%s,%s,%s)"
                #tt=f"{str(datetime.now())[:11]} {int(hours)}:{int(minutes)}:{seconds:.2f}"
                #data=(work,tsk[i],self.userName,sTime,tt)
                hours, remainder = divmod(eTime-sTime, 3600)
                minutes, seconds = divmod(remainder, 60)
                #print(f"Total Time Spent: {int(hours)}h {int(minutes)}m {seconds:.2f}s")
                #self.cursor.execute(querry,data)
                #tt=f"({str(datetime.now())[:4]},{str(datetime.now())[5:7]},{str(datetime.now())[8:10]},{int(hours)},{int(minutes)},{seconds:.2f})"
                #st=f"({str(datetime.now())[:4]},{str(datetime.now())[5:7]},{str(datetime.now())[8:10]},{sTimeHum[:2]},{sTimeHum[3:5]},{sTimeHum[6:8]})"
                tt=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
                st=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
                data=(work,tsk[i],self.userName,st,tt)
                self.cursor.execute(querry,data)
                #print(f"{sTime}:{eTime}")
                self.conn.commit()
                print(f"Total Time Spent: {int(hours)}h {int(minutes)}m {seconds:.2f}s")
                #print(f"Total Time Spent: {tt}")
        else:
            print("Login First...")
            print()
            self.loginUser()
            
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
            self.cursor.execute(f"SELECT * FROM users WHERE userName='{userName}'")
        except:
            print("Invalid Credentials 2")
            exit()
        users=self.cursor.fetchone()
        if passw==users[2]:
            self.userVerified = True
            self.userName=userName
            self.startTime = time.strftime("%H:%M:%S",time.localtime(time.time()))
            print("Login Successful...")
            self.addActivity()
        else:
            print("Invalid Credentials")

        #except:
            #print("Invalid Credentials 2")

    #def addActivity(self):
        #if userVerified == True:
            #task=input(f"""User: {userName} Started at: {self.start_time}
            """
            Enter Category you are working on:
            1. Python
            2. DSA 
            3. SQL
            4. C++
            5. Projects
            6. Linux
            7. Other
            --------------> """

            

        #else:
            #self.loginUser()
            
       

z=input("Enter what you wany to do: ")
x=perpro()
if z=="cu":
    x.create_user()
elif z=="lu":
    x.listUsers()
elif z=="login":
    x.loginUser()
elif z=="tsk":
    x.addActivity()
