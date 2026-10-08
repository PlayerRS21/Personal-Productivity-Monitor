from newScreen import header
import time
from datetime import datetime
import database as db
import variables as v
import categories as c
import os
import json
import threading
import subprocess
from notify import send


def loginCheck():
    if v.userVerified == False:
        print("Login First")
        exit()

class FileRelated:
    def __init__(self,work,category,sTime,brktkn=0,lstme="",ttime=0):
        if len(str(sTime))>22:
            sTime=str(sTime)[:-4]
        self.work=work
        self.category=category
        self.sTime=sTime
        self.breakTaken=brktkn
        self.lastTime=lstme
        self.paused=False
        self.totalTime=ttime
        self.writeToFile()

    def updatelt(self):
        if not self.paused:
            x=datetime.now()
            self.lastTime=str(x)[:-4]
            self.totalTime=self.totalTime+5
            
    def writeToFile(self):
        self.updatelt()
        data={}
        with open(".runningTasks.json","r") as file:
            data=json.load(file)
            
        with open(".runningTasks.json","w") as file:
            data[v.userID]={"taskName":self.work, "category":self.category, "startTime":self.sTime, "lastUpdatedTime":self.lastTime, "totalTime":self.totalTime, "breakTaken":self.breakTaken}
            json.dump(data, file, indent=2)

    def calculateBreak(self):
        if self.paused:
            self.breakTaken=self.breakTaken+5
            # self.writeToFile()

    def loopedwriteToFile(self,var):
        while not var.is_set():
            self.writeToFile()
            time.sleep(5)

    def loopedcalculateBreak(self,var):
        while not var.is_set():
            self.calculateBreak()
            time.sleep(5)

    def breakTimeReturn(self):
        return self.breakTaken

def svData(work,selectCategory,st,et,tt,b):
    query1="INSERT INTO tasks (taskName,category,user_id) VALUES (%s,%s,%s)"
    data=(work,selectCategory,v.userID)
    response=db.DBSaveData(query1,data)
    if response["status"]==True:
        query2="INSERT INTO sessions (user_id, task_id, created_at, ended_at, total_time, break_taken, status) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        lastid=db.getid()
        data=(v.userID,lastid,st,et,tt,b,"Completed")
        response=db.DBSaveData(query2,data)
        if response["status"]==True:
            hours, remainder = divmod(tt, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"Activity Completed in {int(hours)}h {int(minutes)}m {float(seconds)}s")
            with open(".runningTasks.json","r") as file:
                # input(dict(file))/
                data=json.load(file)
                del data[v.userID]
            with open(".runningTasks.json","w") as file:
                # input(data)
                json.dump(data,file,indent=2)
                time.sleep(1)

        else:
            print("Error at Querry2:",querry2)
            print(response["error"])
            exit()
    else:
        print("Error at Querry1:",querry1)
        print(response["error"])
        exit()

            
# Function to add tasks
def addActivity():
    loginCheck()
    while True:
        header()
        print("-"*12)
        print("| Add Task |")
        print("-"*12)
        selectCategory=c.chooseCategory()
        if selectCategory is None:
            break
                
        try:    
            work=input("Enter Task Name: ")
            if work.split()=="":
                print("Incorrect Activity Name.")
                time.sleep(1)
                continue
                
        except ValueError:
            print("Please enter a valid task name.")
            time.sleep(0.6)
            continue
            
        except EOFError:
            print("No input was provided.")
            time.sleep(0.8)
            continue
            
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Returning to main menu.")
            time.sleep(1)
            condition=False
            break
            
        except OSError:
            print("A system input/output error occurred.")
            time.sleep(1)
            condition=False
            break

        if work.lower()=="q":
            print("Returning to main menu")
            time.sleep(1)
            break
                
        # sTime=time.perf_counter()
        sTimeHum=str(time.strftime("%H:%M:%S",time.localtime(time.time())))
        sTime=datetime.now()
        send("Task Started",f"Task Started: {work} at {sTimeHum}")
        print(f"\nTask Started at {sTimeHum}\n")
        helper=FileRelated(work,selectCategory,sTime)
        if not os.path.isfile(".runningTasks.json"):
            with open(".runningTasks.json","w") as file:
                data={}
                json.dump(data,file,indent=2)
                    
        x=threading.Event()
        t1=threading.Thread(target=helper.loopedwriteToFile , args=(x,))
        t1.daemon=True
        t1.start()
        while True:
            try:
                timerTask=input("Press enter to end timer or press 'p' to pause the timer or press 'l' to leave timer to continue later: ")
                    
                if timerTask=="p":
                    print("\nBreak Taken\n")
                    done=threading.Event()
                    t2=threading.Thread(target=helper.loopedcalculateBreak , args=(done,))
                    t2.daemon=True
                    t2.start()
                    end=input("Press 'q' to end timer or press any other key to end break and resume timer or press 'l' to leave timer to continue later: ")
                    if end == "q":
                        done.set()
                        t2.join()
                        helper.writeToFile()
                    elif end=="l":
                        print("You can continue the activity later.")
                        time.sleep(1)
                        exit()
                    else:
                        print("\n\nTimer Started\n\n")
                        helper.paused=False
                        continue
                    
                x.set()
                t1.join()
                break
                
            except KeyboardInterrupt:
                print("Saving Timer")
                break

            except:
                pass

        # eTime=time.perf_counter()
        # et=datetime.now()
        # eTimeHum=str(time.strftime("%H:%M:%S",time.localtime(time.time())))
        # hours, remainder = divmod(eTime-sTime, 3600)
        # minutes, seconds = divmod(remainder, 60)
        # tt=int(eTime-sTime)
        # et=f"{str(datetime.now())[:10]} {eTimeHum[:2]}:{eTimeHum[3:5]}:{eTimeHum[6:8]}"
        # st=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
        svData(helper.work,helper.category,helper.sTime,helper.lastTime,helper.totalTime,helper.breakTaken)
        print("Done...")
        time.sleep(2)
        break
        # query="INSERT INTO tasks (taskName,category,user_id) VALUES (%s,%s,%s)"
        # data=(work,selectCategory,v.userID)
        # response=db.DBSaveData(query,data)
            
        # if response["status"]==True:
            # query="INSERT INTO sessions (user_id, task_id, created_at, ended_at, total_time, breakTime, status) VALUES (%s,%s,%s,%s,%s,%s)"
            # lastid=db.getid()
            # data=(v.userID,lastid,st,et,tt,helper.breakTimeReturn(),"Completed")
            # response=db.DBSaveData(query,data)
            # if response["status"]==True:
                # print(f"Activity Completed in {int(hours)}h {int(minutes)}m")
                # with open(".runningTasks.json","r") as file:
                    # data=json.load(file)
                    # del data[v.userID]
                # with open(".runningTasks.json","w") as file:
                    # json.dump(data,file,indent=2)
                    # time.sleep(1)
                    # break

            # else:
            # print("Error at 2nd cmd")
                # print(response["error"])
                # exit()
        # else:
            # print("Error at 1st cmd")
            # print(response["error"])
            # exit()


def loadTask():
    try:
        with open(".runningTasks.json","r") as file:
            tasks=json.load(file)
            if v.userID in tasks:
                return {"found":True,"data":tasks[v.userID]}
            else:
                return {"found":False,"data":""}

    except FileNotFound:
        return {"found":False,"data":""}


def saveTask():
    task=loadTask()
    if task["found"]==True:
        data=task["data"]
        hours, remainder = divmod(data["totalTime"], 3600)
        minutes, seconds = divmod(remainder, 60)
        svData(data["taskName"],data["category"],data["startTime"],data["lastUpdatedTime"],data["totalTime"],data["breakTaken"])

    addActivity()

def resumeTask():
    data = loadTask()
    if data["found"]==False:
        print("No unsaved activity found")
        exit()
    data = data["data"]
    # {'taskName','category','startTime','lastUpdatedTime','totalTime','breakTaken'}
    helper=FileRelated(data["taskName"],data["category"],data["startTime"],data["breakTaken"],data["lastUpdatedTime"],data["totalTime"])
    send("Task Resumed",f"Task Started: {data["taskName"]}")
    print("\nTask Resumed\n")
    if not os.path.isfile(".runningTasks.json"):
        with open(".runningTasks.json","w") as file:
            data={}
            json.dump(data,file,indent=2)

    x=threading.Event()
    t1=threading.Thread(target=helper.loopedwriteToFile , args=(x,))
    t1.daemon=True
    t1.start()
    while True:
        try:
            timerTask=input("Press enter to end timer or press 'p' to pause the timer or press 'l' to leave timer to continue later: ")

            done=threading.Event()
            t2=threading.Thread(target=helper.loopedcalculateBreak , args=(done,))
            t2.daemon=True
            if timerTask=="p":
                helper.paused=True
                print("\nBreak Taken\n")
                t2.start()
                end=input("Press 'q' to end timer or press any other key to end break and resume timer ")
                if end == "q":
                    done.set()
                    t2.join()
                    helper.writeToFile()
                elif end =="l":
                    print("You can continue the activity later.")
                    time.sleep(1)
                    exit()
                else:
                    print("\n\nTimer Started\n\n")
                    helper.paused=False
                    continue

        except Exception as e:
            print(e)
            exit()
                
        print("Saving Timer")
        x.set()
        t1.join()
        svData(helper.work,helper.category,helper.sTime,helper.lastTime,helper.totalTime,helper.breakTaken)
        print("Activity Saved")
        time.sleep(2)
        break
            
if __name__=="__main__":
    # addActivity()
    resumeTask()
