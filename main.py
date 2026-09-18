import mysql.connector
from mysql.connector import Error
import time
from datetime import datetime
import os
import sys

class ProductivityMonitor:
    __logo="""    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Productivity Monitor           |           
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """
    userVerified=False
    userName=""
    startTime=""
    items=0
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
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,userName VARCHAR(50) NOT NULL UNIQUE,password VARCHAR(100) NOT NULL,created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,last_login TIMESTAMP DEFAULT NULL)")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INT AUTO_INCREMENT UNIQUE,taskName VARCHAR(100) NOT NULL,category VARCHAR(100) NOT NULL,created_by VARCHAR(50),created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,total_time TIMESTAMP NOT NULL);")
            #print("Successfully connected to MariaDB server!")
            self.initial()

        except mysql.connector.Error as e:
            print(f"Error connecting to Database: {e}")
            exit()

    def initial(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.__logo)
        print("Enter Your Choice: ")
        i=input("1. Login\n2. Register\n'e' to exit: ")
        if i=="1":
            self.loginUser()
        elif i=="2":
            self.createUser()
        else:
            print("Thanks For Using The App.")
            exit()

    def addActivity(self):
        print("Add Task:")
        if self.userVerified == True:
            tsk=["Python","DSA","SQL","C++","Projects","Linux","Collage Work","Other"]
            print(f"User:{self.userName}--------------Login at:{self.startTime}")
            print("Select Category: ")
            for i in range(len(tsk)):
                print(f"{i+1}. {tsk[i]}")
            print()
            try:
                i=input("--> ")
                i=int(i)
            except KeyboardInterrupt:
                print("Returning to Main Menu")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.whattodo()
            except:
                if i=="e":
                    print("Returning to Main Menu")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(self.__logo)
                    self.whattodo()
                print("Wront Choice.")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
            if i>len(tsk):
                print("Incorrect Choice.")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.addActivity()
            work=input("Enter Task Name: ")
            sTime=time.perf_counter()
            sTimeHum=str(time.strftime("%H:%M:%S",time.localtime(time.time())))
            print(f"Task Started at {sTimeHum}\nPress Ctrl + C to exit.")
            try:
                input("")
                e
            except:
                eTime=time.perf_counter()
                querry="INSERT INTO tasks (taskName,category,created_by,created_on,total_time) VALUES (%s,%s,%s,%s,%s)"
                hours, remainder = divmod(eTime-sTime, 3600)
                minutes, seconds = divmod(remainder, 60)
                tt=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
                st=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
                data=(work,tsk[i-1],self.userName,st,tt)
                self.cursor.execute(querry,data)
                self.conn.commit()
                print(f"Total Time: {int(hours)}h {int(minutes)}m {seconds:.2f}s")
                print("Returning to main menu")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.whattodo()
        else:
            print("Login First...")
            print()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.loginUser()
            
    def createUser(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.__logo)
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

    def viewActivity(self):
        print(f"User:{self.userName}--------------Login at:{self.startTime}")
        items=0
        if self.userVerified!=True:
            print("Login First...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.loginUser()
            return
        querry=f"SELECT * FROM tasks WHERE created_by='{self.userName}'"
        self.cursor.execute(querry)
        tsk=self.cursor.fetchall()
        if tsk!=[]:
            for i in range(len(tsk)):
                items=items+1
                print(f"{i+1}. {tsk[i][1]}")
            self.items=items
            input("Press 'enter' to go back")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        else:
            input("No tasks done yet.\nPress 'Enter' to continue.")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()

    def updateActivity(self):
        print(f"User:{self.userName}--------------Login at:{self.startTime}")
        if self.userVerified!=True:
            print("User Not Logged in.")
            time.sleep(1)
            self.loginUser()
            return
        querry=f"SELECT * FROM tasks WHERE created_by='{self.userName}'"
        self.cursor.execute(querry)
        querry=self.cursor.fetchall()
        if querry==[]:
            print("No Tasks To Display.")
            input("Press Enter To Continue.")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][1]}")
        try:
            wtsk=input("Enter Which Activity you want to modify: ")
            wtsk=int(wtsk)
        except KeyboardInterrupt:
            print("Returning to main menu")
            time.sleep(0.4)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        except:
            if wtsk=="e":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.whattodo()
            print("Wrong Input...")
            time.sleep(0.7)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.updateActivity()
        if wtsk>len(querry) or wtsk<0:
            print("Wrong Choice.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.updateActivity()
        tskid=querry[wtsk-1][0]
        todo=["Update Name","Update Category"]
        for i in range(len(todo)):
            print(f"{i+1}. {todo[i]}")
        try:
            whattochange=int(input("Enter what you want to change:"))
        except:
            print("Incorrect Input")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.updateActivity()
        if whattochange==1:
            newname=input("Enter New Name to set.\n: ")
            querry=f"UPDATE tasks SET taskName='{newname}' WHERE id={tskid}"
            try:
                self.cursor.execute(querry)
                self.conn.commit()
                print("Done...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.whattodo()
            except mysql.connector.Error as e:
                print("Error Occured:\n"+e)
                
    def deleteActivity(self):
        if self.userVerified==False:
            print("User Not Logged in.")
            time.sleep(1)
            self.loginUser()
        querry=f"SELECT * FROM tasks WHERE created_by='{self.userName}'"
        self.cursor.execute(querry)                                                                                           
        querry=self.cursor.fetchall()
        if querry==[]:
            print("No Tasks To Display.")
            input("Press Enter To Continue.")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][1]}")
        try:
            wtsk=input("Enter Which Activity you want to delete: ")
            wtsk=int(wtsk)
        except KeyboardInterrupt:
            print("Returning to main menu")
            time.sleep(0.4)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        except:
            if wtsk=="e":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.whattodo()
            print("Wrong Input...")
            time.sleep(0.7)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.updateActivity()
        if wtsk>len(querry) or wtsk<0:
            print("Wrong Choice.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.updateActivity()
        tskid=querry[wtsk-1][0]
        suretodelete=input("Are you sure you want to delete(y/N) ")
        if suretodelete.lower()=="y":
            querry=f"DELETE FROM tasks WHERE id={tskid}"
            try:
                self.cursor.execute(querry)
                self.conn.commit()
                print("Task Deleted.")
                input("Press a key to continue.")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.whattodo()
            except mysql.connector.Error as e:
                print("Error Occured:\n"+e)
        else:
            print("Task Not Deleted.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        
    def whattodo(self):
        print(f"User:{self.userName}--------------Login at:{self.startTime}")
        newchoice=["Add New Task","View Previous Tasks","Update Activity","Delete Activity","Search Activity","View Statistics","Logout"]
        print("Enter your choice: ")
        for i in range(len(newchoice)):
            print(f"{i+1}. {newchoice[i]}")
        try:
            i=int(input("→ "))
        except ValueError:
            print("Invalid Choice...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        if (i>len(newchoice) or i<0):
            print("Invalid Choice")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        elif i==1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.addActivity()
        elif i==2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.viewActivity()
        elif i==3:
            pass
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.updateActivity()
        elif i==4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.deleteActivity()
        elif i==5:
            return
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.searchActivity()
        elif i==6:
            return
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.viewStat()
        elif i==7:
            x=input("Sure to Logout?(Y/n) ")
            if x.lower()=="y" or x.lower()=="":
                self.userName=""
                self.userVerified=False
                self.startTime=""
                self.items=0
                print("Logout Done.\nRedirecting to login.")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.initial()
        else:
            print("Wrong Input...")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.whattodo()
        
    def loginUser(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.__logo)
        userName=input("Enter Your User Name: ")
        passw=input("Enter Your Password: ")
        self.cursor.execute(f"SELECT * FROM users WHERE userName='{userName}'")
        users=self.cursor.fetchone()
        if users==None:
            print("Invalid Credentials.\nIf you are a new user try creating a new user.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.loginUser()
        if passw==users[2]:
            self.userVerified = True
            self.userName=userName
            self.startTime = time.strftime("%H:%M:%S",time.localtime(time.time()))
            sTimeHum=str(self.startTime)
            t=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
            querry=f"UPDATE users SET last_login='{t}' WHERE userName='{userName}'"
            try:
                self.cursor.execute(querry)
                self.conn.commit()
                print("Login Successful...")
                time.sleep(0.4)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.__logo)
                self.whattodo()
            except mysql.connector.Error as e:
                print(e)
        else:
            print("Invalid Credentials. Try Again.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.__logo)
            self.loginUser()

x=ProductivityMonitor()
