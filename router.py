import time
import startTask as st
import viewTask as vw
from newScreen import header
import updateTask as up
import deleteTask as de
import searchTask as se
import statistics as stat
import variables as v


def loginCheck():
    if v.userVerified == False:
        print("Login First")
        exit()

# Routes to every function
def router():
    loginCheck()
    while True:
        header()
        newchoice=["Add New Task","View Previous Tasks","Update Activity","Delete Activity","Search Activity","View Statistics","Logout"]
        print("Enter your choice: ")
        for i in range(len(newchoice)):
            print(f"{i+1}. {newchoice[i]}")
        try:
            choice=input("press 'q' to quit or Enter your choice: ")
            choice=int(choice)
            
        except ValueError:
            if choice == "q":
                print("Returning to Main Menu")
                time.sleep(1)
                break
                
            print("Please enter a number.")
            time.sleep(1)
            continue
        
        except EOFError:
            print("No input was provided.")
            time.sleep(1)
            continue
        
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Routing Back to Login.")
            time.sleep(0.7)
            break
        
        except OSError:
            print("A system input/output error occurred.")
            break
            
        if (choice>len(newchoice) or choice<0):
            print("Invalid Choice")
            time.sleep(1)
            continue
            
        elif choice==1:
            st.addActivity()
            
        elif choice==2:
            vw.viewActivity()
            
        elif choice==3:
            up.updateActivity()
            
        elif choice==4:
            de.deleteActivity()
            
        elif choice==5:
            se.searchActivity()
            
        elif choice==6:
            stat.viewStatistics()
            
        elif choice==7:
            x=input("Sure to Logout?(Y/n) ")
            if x.lower()=="y" or x.lower()=="":
                v.userName=""
                v.userVerified=False
                v.startTime=""
                print("Logout Done.\nRedirecting to login.")
                time.sleep(1)
                break
        else:
            print("Wrong Input...")
            time.sleep(1)
            continue
