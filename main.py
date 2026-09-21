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
    tsk=["Python","DSA","SQL","C++","Projects","Linux","Collage Work","Other"]
    # Check Whether Database is working or not
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
            # self.cursor.execute("DROP DATABASE productivityMonitor")
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS productivityMonitor")
            self.cursor.execute("USE productivityMonitor")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,userName VARCHAR(50) NOT NULL UNIQUE,email VARCHAR(70) NOT NULL UNIQUE,password VARCHAR(100) NOT NULL,created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,last_login TIMESTAMP DEFAULT NULL)")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INT AUTO_INCREMENT UNIQUE,taskName VARCHAR(100) NOT NULL,category VARCHAR(100) NOT NULL,created_by VARCHAR(50),created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,total_time TIMESTAMP NOT NULL);")
            #print("Successfully connected to MariaDB server!")
            self.initial()

        except mysql.connector.Error as e:
            print(f"Error connecting to Database: {e}")
            exit()

    # Checking is the user new or old via login and register
    def initial(self):
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print(self.__logo)
        self.newScreen()
        print("Enter Your Choice: ")
        i=input("1. Login\n2. Register\n'e' to exit: ")
        if i=="e":
            print("Thanks For Using The App.")
            exit()
        elif i=="1":
            self.loginUser()
        elif i=="2":
            self.createUser()
        else:
            print("Wrong Input \nPress 'q' to exit.")
            self.initial()

    def newScreen(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print(self.__logo)
        if self.userVerified==True:
            print(f"User: {self.userName}-------------------Login at:{self.startTime}")
            print()

    # Function to add tasks
    def addActivity(self):
        self.newScreen()
        print("Add Task:")
        if self.userVerified == True:
            # print(f"User:{self.userName}--------------Login at:{self.startTime}")
            print("Select Category: ")
            for i in range(len(self.tsk)):
                print(f"{i+1}. {self.tsk[i]}")
            print()
            try:
                i=input("--> ")
                i=int(i)
            except KeyboardInterrupt:
                print("Returning to Main Menu")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.newScreen()
                self.whattodo()
            except:
                if i=="e":
                    print("Returning to Main Menu")
                    time.sleep(1)
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    # print(self.__logo)
                    self.newScreen()
                    self.whattodo()
                print("Wrong Choice.")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.newScreen()
            if i>len(self.tsk):
                print("Incorrect Choice.")
                time.sleep(0.5)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.newScreen()
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
                tt=f"{str(datetime.now())[:10]} {int(hours)}:{int(minutes)}:{int(seconds)}"
                st=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
                data=(work,self.tsk[i-1],self.userName,st,tt)
                self.cursor.execute(querry,data)
                self.conn.commit()
                print(f"Total Time: {int(hours)}h {int(minutes)}m {seconds:.2f}s")
                print(tt)
                print("Returning to main menu")
                # time.sleep(2)
                input()
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.newScreen()
                self.whattodo()
        else:
            print("Login First...")
            print()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.loginUser()


    # Function to create new user
    def createUser(self):
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print(self.__logo)
        self.newScreen()
        em=input("Enter Email: ")
        uName=input("Enter User Name: ")
        p=input("Enter Password or default will be 1234: ")
        querry="INSERT INTO users (userName,email,password) VALUES (%s,%s,%s)"
        if p !="":
            data=(uName,em,p)
        elif p=="":
            data=(uName,em,"1234")
        try:
            self.cursor.execute(querry,data)
            self.conn.commit()
            print(f"User \"{uName}\" is created.")

        # 1062 (23000): Duplicate entry 'raja' for key 'userName'
        
        except mysql.connector.Error as e:
            print(e)
            e=str(e)
            if "Duplicate entry" in e:
                if "userName" in e:
                    print("UserName Already in use")
                    self.createUser()
                elif "email" in e:
                    print("Email Already in use")
                    self.createUser()
                else:
                    print(e)

    # Function to View Tasks Done
    def viewActivity(self):
        # print(f"User:{self.userName}--------------Login at:{self.startTime}")
        self.newScreen()
        if self.userVerified!=True:
            print("Login First...")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # self.loginUser()
            self.newScreen()
            return
        querry=f"SELECT * FROM tasks WHERE created_by='{self.userName}'"
        self.cursor.execute(querry)
        querry=self.cursor.fetchall()
        if self.tsk!=[]:
            # items=0
            for i in range(len(querry)):
                # items=items+1
                print(f"{i+1}. {querry[i][1]}     :      {querry[i][2]}")
            # self.items=items
            input("Press 'enter' to go back")
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()
        else:
            input("No tasks done yet.\nPress 'Enter' to continue.")
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()


    # Function to Search Tasks
    def searchActivity(self):
        self.newScreen()
        # print(f"User:{self.userName}--------------Login at:{self.startTime}")
        i=input("Search via name: ")
        try:
            querry=f"SELECT taskName,category,created_by FROM tasks WHERE (taskname LIKE '%{i}' OR taskName LIKE '{i}%' OR taskName LIKE '%{i}%' OR taskName LIKE '%{i.lower()}' OR taskName LIKE '{i.lower()}%' OR taskName LIKE '%{i.lower()}%') AND created_by ='{self.userName}'"
            self.cursor.execute(querry)
            querry=self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
            exit()
        if querry == []:
            print("No Results Found want to search via category? (Y/n) ")
            x=input()
            if x.lower()=="y" or x.lower()=="":
                for i in range(len(self.tsk)):
                    print(f"{i}. {self.tsk[i]}")
            x=input("Choose Category: ")
            try:
                x=int(x)
            except:
                print("Wrong Input.")
                time.sleep(0.7)
                # os.system('cls' if os.name=='nt' else 'clear')
                # print(self.__logo)
                # self.newScreen()
                self.searchActivity()
                        
            if x>len(self.tsk) or x<0:
                print("Wrong Input.")
                time.sleep(0.7)
                search(querry)
                querry=f"SELECT (taskName,category,created_by) FROM tasks WHERE category='{self.tsk[x-1]}' AND created_by ='{self.userName}'"
                self.cursor.execute(querry)
                querry=self.cursor.fetchall()
        if querry ==[]:
            print("No Record Found Try Again With Different Filters...")
            time.sleep(2)
            # os.system('cls' if os.name=='nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][0]}    :     {querry[i][1]}")
        input("Press Enter To Continue. ")
        # os.system('cls' if os.name=='nt' else 'clear')
        # print(self.__logo)
        # self.newScreen()
        self.whattodo()

    # Function to Update Activity
    def updateActivity(self):
        self.newScreen()
        # print(f"User:{self.userName}--------------Login at:{self.startTime}")
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
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][1]}   :   {querry[i][2]}")
        try:
            wtsk=input("Enter Which Activity you want to modify: ")
            wtsk=int(wtsk)
        except KeyboardInterrupt:
            print("Returning to main menu")
            time.sleep(0.4)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()
        except:
            if wtsk=="e":
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                # self.newScreen()
                self.whattodo()
            print("Wrong Input...")
            time.sleep(0.7)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.updateActivity()
        if wtsk>len(querry) or wtsk<0:
            print("Wrong Choice.")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
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
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.updateActivity()
        if whattochange==1:
            newname=input("Enter New Name to set.\n: ")
            querry=f"UPDATE tasks SET taskName='{newname}' WHERE id={tskid}"
            try:
                self.cursor.execute(querry)
                self.conn.commit()
                print("Done...")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                # self.newScreen()
                self.whattodo()
            except mysql.connector.Error as e:
                print("Error Occured:\n"+e)

        elif whattochange==2:
            # self.newScreen()
            print("Choose new category: ")
            # tsk=["Python","DSA","SQL","C++","Projects","Linux","Collage Work","Other"]
            for i in range(len(self.tsk)):
                print(f"{i+1}. {self.tsk[i]}")
            print()
            try:
                i=input("--> ")
                i=int(i)
            except KeyboardInterrupt:
                print("Returning to Main Menu")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.whattodo()
            except:
                if i=="e":
                    print("Returning to Main Menu")
                    time.sleep(1)
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    # print(self.__logo)
                    self.whattodo()
                print("Wront Choice.")
                time.sleep(1)
                self.updateActivity()
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
            if i>len(tsk):
                print("Incorrect Choice.")
                time.sleep(0.5)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                # self.addActivity()
                self.updateActivity()
            querry=f"UPDATE tasks SET category='{self.tsk[i-1]}' WHERE id={tskid}"
            try:
                self.cursor.execute(querry)
                self.conn.commit()
                print("Done...")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.whattodo()
            except mysql.connector.Error as e:
                print(e)

    # Function to Delete Task
    def deleteActivity(self):
        self.newScreen()
        # print(f"User:{self.userName}--------------Login at:{self.startTime}")
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
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.whattodo()
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][1]}")
        try:
            wtsk=input("Enter Which Activity you want to delete: ")
            wtsk=int(wtsk)
        except KeyboardInterrupt:
            print("Returning to main menu")
            time.sleep(0.4)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.whattodo()
        except:
            if wtsk=="e":
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.whattodo()
            print("Wrong Input...")
            time.sleep(0.7)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.updateActivity()
        if wtsk>len(querry) or wtsk<0:
            print("Wrong Choice.")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
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
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.whattodo()
            except mysql.connector.Error as e:
                print("Error Occured:\n"+e)
        else:
            print("Task Not Deleted.")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.whattodo()

    # Function to Route User
    def whattodo(self):
        self.newScreen()
        # print(f"User:{self.userName}--------------Login at:{self.startTime}")
        newchoice=["Add New Task","View Previous Tasks","Update Activity","Delete Activity","Search Activity","View Statistics","Logout"]
        print("Enter your choice: ")
        for i in range(len(newchoice)):
            print(f"{i+1}. {newchoice[i]}")
        try:
            i=int(input("→ "))
        except ValueError:
            print("Invalid Choice...")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.whattodo()
        if (i>len(newchoice) or i<0):
            print("Invalid Choice")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.whattodo()
        elif i==1:
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.addActivity()
        elif i==2:
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.viewActivity()
        elif i==3:
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.updateActivity()
        elif i==4:
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.deleteActivity()
        elif i==5:
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.searchActivity()
        elif i==6:
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
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
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.initial()
        else:
            print("Wrong Input...")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.whattodo()

    # Function to login user
    def loginUser(self):
        self.newScreen()
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print(self.__logo)
        userName=input("Enter Your User Name: ")
        passw=input("Enter Your Password: ")
        self.cursor.execute(f"SELECT * FROM users WHERE userName='{userName}'")
        users=self.cursor.fetchone()
        if users==None:
            print("Invalid Credentials.\nIf you are a new user try creating a new user.")
            time.sleep(2)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.loginUser()
        if passw==users[3]:
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
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.whattodo()
            except mysql.connector.Error as e:
                print(e)
        else:
            print("Invalid Credentials. Try Again.")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            self.loginUser()

    # Fubction to View Statistics
    def viewStat(self):
        self.newScreen()
        querry=f"SELECT SUM(total_time) FROM tasks WHERE created_by=%s AND category=%s"
        print(" Total Productivity ")
        print("-"*32)
        th,tm,ts=0,0,0
        for i in range(len(self.tsk)):
            data=(self.userName,self.tsk[i])
            self.cursor.execute(querry,data)
            lst=self.cursor.fetchone()
            if lst[0]!=None:
                print(f"{self.tsk[i]}:"," "*(30-8-(len(self.tsk[i]))),end="")
                lst=lst[0]
                lst=str(lst)
                lst=lst[-6:]
                # print(lst)
                h , m , s = [lst[i:i+2] for i in range(0, len(lst), 2)]
                th=th+int(h)
                tm=tm+int(m)
                ts=ts+int(s)
                print(f"{h}h {m}m")

        print("-"*32)
        while ts>60:
            ts=ts-60
            tm=tm+1
        while tm>60:
            tm=tm-60
            th=th+1
        
        print("Total"," "*(30-6-8),f"{th}h {tm}m {ts}s")

x=ProductivityMonitor()


