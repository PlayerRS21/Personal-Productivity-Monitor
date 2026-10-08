from newScreen import header
import variables as v
from datetime import datetime,date
import database as db
from viewTask import listtasks
import categories as c
import time



minimumDate=""
maximumDate=""


def loginCheck():
    global maximumDate
    global minimumDate
    if v.userVerified == False:
        print("Login First")
        exit()

    querry="SELECT MIN(created_at) FROM sessions WHERE user_ID=%s"
    data=(v.userID,)
    minimumDate=db.DBExecute(querry,data)
    minimumDate=str(minimumDate[0][0])[:11]
    querry="SELECT MAX(created_at) FROM sessions WHERE user_ID=%s"
    maximumDate=db.DBExecute(querry,data)
    maximumDate=str(maximumDate[0][0])[:11]

# print(maximumDate,minimumDate)
# input()
categories=c.listAllCategories("name_id")

# Function to view Daily Statstics
def viewStatDaily():
    header()
    query="SELECT tasks.id, tasks.category, SUM(sessions.total_time) FROM tasks INNER JOIN sessions on tasks.id=sessions.task_id WHERE tasks.user_ID=%s AND category=%s AND created_at >= CURDATE()  AND created_at <= NOW()"
    print("Today's Productivity")
    print("-"*20)
    totalTime=0
    for key,value in categories.items():
        data=(v.userID,key)
        response = db.DBExecute(query,data)        
        
        if response[0][0]!=None:
            totalTime=totalTime+response[0][2]
            hours, remainder = divmod(response[0][2], 3600)
            minutes, seconds = divmod(remainder, 60)
            
            if minutes==0 and hours == 0:
                print(f"{value}  {seconds}s")

            elif hours==0:
                print(f"{value}  {minutes}m {seconds}s")

            else:
                print(f"{value}  {hours}h {minutes}m {seconds}s")

    hours, remainder = divmod(totalTime, 3600)
    minutes, seconds = divmod(remainder, 60)
    print("Total Productivity  ",end="")
    if minutes==0 and hours==0:
        print(f"{seconds}s")
    elif hours==0:
        print(f"{minutes}m {seconds}s")
    else:
        print(f"{hours}h {minutes}m {seconds}s")
                
    print("-"*20)    

def viewStatMonthly():
    global maximumDate
    global minimumDate
    year=int(str(maximumDate[:4]))
    month=1
    tempmaxDate=int(str(maximumDate[5:7]))
    header()
    querry = "SELECT tasks.id, tasks.category, SUM(sessions.total_time) FROM tasks INNER JOIN sessions on tasks.id=sessions.task_id WHERE tasks.user_ID=%s AND category=%s AND created_at >= %s AND created_at <= %s"
    print(" ","="*25)
    print(" ||  Monthly Productivity || ")
    print(" ","="*25)
    monthlist=["January","Febuary","March","April","May","June","July","August","September","October","November","December"]    
    totalTime=0
    while month<=tempmaxDate:
        print("-"*30)
        print(f"{monthlist[month-1]} {year} Productivity")
        for key,value in categories.items():
            if month<10:
                extra=f"{year}-0{month}-01"
                extraDate=f"{year}-{month+1}-01"
            else:
                extra=f"{year}-{month}-01"
                extraDate=f"{year}-{month+1}-01"

            data=(v.userID,key,extra,extraDate)
            response=db.DBExecute(querry,data)
            if response[0][0]!=None:
                totalTime=totalTime+response[0][2]
                hours, remainder = divmod(response[0][2], 3600)
                minutes, seconds = divmod(remainder, 60)
        
                if minutes==0 and hours==0:
                    print(f"{value}  {seconds}s")
        
                elif hours==0:
                    print(f"{value}  {minutes}m {seconds}s")
        
                else:
                    print(f"{value}  {hours}h {minutes}m {seconds}s")

        hours, remainder = divmod(totalTime, 3600)
        minutes, seconds = divmod(remainder, 60)
        print("Total Productivity  ",end="")
        if minutes==0 and hours==0:
            print(f"{seconds}s")
        elif hours==0:
            print(f"{minutes}m {seconds}s")
        else:
            print(f"{hours}h {minutes}m {seconds}s")
            
        month=month+1
        print("-"*30)
        print()


# Fubction to view Yearly Statistics
def viewStatYearly():
    # global minimumDate
    # global maximumDate
    tempminDate=int(str(minimumDate[:4]))
    header()
    querry="SELECT tasks.id, tasks.category, SUM(sessions.total_time) FROM tasks INNER JOIN sessions on tasks.id=sessions.task_id WHERE tasks.user_ID=%s AND tasks.category=%s AND created_at >= %s AND created_at < %s"
    print(" ","="*25)
    print(" ||  Yearly Productivity  ||")
    print(" ","="*25)
    while tempminDate<=int(str(maximumDate[:4])):
        print("-"*30)
        extra=f"{tempminDate}-01-01"
        maxd=f"{tempminDate+1}-12-31"
        print(f"{tempminDate} Year's Productivity")
        totalTime=0
        for key,value in categories.items():
            data=(v.userID,key,str(extra),str(maxd))
            response=db.DBExecute(querry,data)

            if response[0][2]!=None:
                totalTime=totalTime+response[0][2]
                hours, remainder = divmod(response[0][2], 3600)
                minutes, seconds = divmod(remainder, 60)

                if minutes==0 and hours==0:
                    print(f"{value}  {seconds}s")

                elif hours==0:
                    print(f"{value}  {minutes}m {seconds}s")
    
                else:
                    print(f"{value}  {hours}h {minutes}m {seconds}s")
                    
        hours, remainder = divmod(totalTime, 3600)
        minutes, seconds = divmod(remainder, 60)
        print("Total Productivity  ",end="")
        
        if minutes==0 and hours==0:
            print(f"{seconds}s")
        elif hours==0:
            print(f"{minutes}m {seconds}s")
        else:
            print(f"{hours}h {minutes}m {seconds}s")
            
        tempminDate=tempminDate+1
        print("-"*30)
        print()

# Fubction to view Weekly Statistics
def viewStatWeekly():
    header()
    query="SELECT tasks.id, tasks.user_ID, tasks.category, SUM(sessions.total_time) FROM tasks JOIN sessions ON tasks.id = sessions.task_id WHERE tasks.user_ID = %s AND tasks.category = %s AND created_at >= %s AND created_at < %s"
    print(" ","="*25)
    print(" ||  Weekly Productivity  ||")
    print(" ","="*25)
    t=datetime.now()
    day=t.day
    month=t.month
    year=t.year
    d=date(year, month, day)
    dayNumber=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    dn=d.strftime("%A")
    dind=dayNumber.index(dn.lower())
    total=0
    for i in range(dind+1):
        tmp=day
        tmp=(tmp-dind)+i
        lstdt=tmp-1
        totalTime=0
        print(dayNumber[i].capitalize(),":")
        print("-"*30)
        for key,value in categories.items():
            dateNormal=f"{year}-{month}-{tmp}"
            datelst=f"{year}-{month}-{lstdt}"
            data=(v.userID,key,datelst,dateNormal)
            # print(data)
            response=db.DBExecute(query,data)
            # print(response)
            if response==[]:
                continue
                    
            elif response[0][0]!=None:
                totalTime=totalTime+response[0][3]
                hours, remainder = divmod(response[0][3], 3600)
                minutes, seconds = divmod(remainder, 60)
                print(categories[response[0][2]],end=" ")
                if minutes==0 and hours==0:
                    print(f"{seconds}s")
                elif hours==0:
                    print(f"{minutes}m {seconds}s")
                else:
                    print(f"{hours}h {minutes}m {seconds}s")

        hours, remainder = divmod(totalTime, 3600)
        minutes, seconds = divmod(remainder, 60)
        total=total+totalTime
        print("Total Productivity: ",end="")
        if minutes==0 and hours==0:
            print(f"{seconds}s")
        elif hours==0:
            print(f"{minutes}m {seconds}s")
        else:
            print(f"{hours}h {minutes}m {seconds}s")

        lstdt=lstdt+1
        print("-"*30)
        print()
    hours, remainder = divmod(total, 3600)
    minutes, seconds = divmod(remainder, 60)
    print("Total Productivity: ",end="")
    if minutes==0 and hours==0:
        print(f"{seconds}s")
    elif hours==0:
        print(f"{minutes}m {seconds}s")
    else:
        print(f"{hours}h {minutes}m {seconds}s")


def viewStatistics():
    loginCheck()
    while True:
        header()
        print("View Statistics on basis of:")
        
        try:
            userChoice=input("1. Today's Statistics\n2. Monthly Statistics\n3. Yearly Statistics\n4.Weekly Statistics\n--> ")
            userChoice=int(userChoice)
        
        except ValueError:
            if userChoice=="q":
                print("Returning to Main Menu")
                time.sleep(1)
                break
                
            print("Please enter a valid whole number.")
            time.sleep(1)
            continue
        
        except EOFError:
            print("No input was provided.")
            time.sleep(1)
            continue
        
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Returning to Main Menu")
            time.sleep(1)
            break
        
        except OSError:
            print("A system input/output error occurred.")
            print("Returning to Main Menu")
            time.sleep(1)
            break

        if userChoice == 1:
            viewStatDaily()
            input("Press 'enter' to continue ")
            break
            
        elif userChoice == 2:
            viewStatMonthly()
            input("Press 'enter' to continue ")
            break
            
        elif userChoice == 3:
            viewStatYearly()
            input("Press 'enter' to continue ")
            break

        elif userChoice == 4:
            viewStatWeekly()
            input("Press 'enter' to continue ")
            break
            
        else:
            print("Please Select a valid number.")
            time.sleep(1)
            continue
        
    
if __name__=="__main__":
    viewStatistics()
