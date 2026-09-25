from newScreen import header
import time
from datetime import datetime
import database as db
import variables as v
import categories as c

def loginCheck():
    if v.userVerified == False:
        print("Login First")
        exit()

# Function to add tasks
def addActivity():
    loginCheck()
    condition=True
    while condition:
        header()
        print("-"*12)
        print("| Add Task |")
        print("-"*12)
        if v.userVerified == True:
            print("Select Category: \n")
            i=1
            for key in c.allCategories.values():
                print(f" {i}. {key}")
                i+=1
            print()

            try:
                selectCategory=input("--> ")
                selectCategory=int(selectCategory)
            
            except ValueError:
                if selectCategory=="e":
                    print("Exiting...")
                    time.sleep(1)
                    condition=False
                    break
        
            except EOFError:
                print("No input was provided.")
                time.sleep(1)
                continue
        
            except KeyboardInterrupt:
                print("\nInput cancelled by the user.")
                print("Returning to main menu.")
                time.sleep(1)
                condition=False
                break
        
            except OSError:
                print("A system input/output error occurred.")
                condition =False
                break

            if selectCategory>len(c.allCategories):
                print("Incorrect Choice.")
                time.sleep(0.5)
                continue

            try:    
                work=input("Enter Task Name: ")
                
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
                timw.sleep(1)
                condition=False
                break
            
            except OSError:
                print("A system input/output error occurred.")
                time.sleep(1)
                condition=False
                break
                
            sTime=time.perf_counter()
            sTimeHum=str(time.strftime("%H:%M:%S",time.localtime(time.time())))
            print(f"Task Started at {sTimeHum}\nPress Ctrl + C to exit.")
            
            try:
                input("")
            except:
                time.sleep(1)

            eTime=time.perf_counter()
            query="INSERT INTO tasks (taskName,category,user_id,created_on,total_time) VALUES (%s,%s,%s,%s,%s)"
            hours, remainder = divmod(eTime-sTime, 3600)
            minutes, seconds = divmod(remainder, 60)
            tt=eTime-sTime
            st=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
            
            data=(work,selectCategory+100,v.userID,st,int(tt))
            response=db.DBSaveData(query,data)
            if response["status"]==True:
                print(f"Activity Completed in {int(hours)}h {int(minutes)}m")
                time.sleep(1)
                break
            
        else:
            print("Login First...")
            exit()
            
if __name__=="__main__":
    addActivity()
