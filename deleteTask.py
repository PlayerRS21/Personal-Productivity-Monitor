from newScreen import header
import variables as v
import database as db
import time
from viewTask import listtasks


def loginCheck():
    if v.userVerified == False:
        print("Login First")
        exit()

# Function to Delete Task
def deleteActivity():
    loginCheck()
    while True:
        header()
        if v.userVerified==False:
            print("User Not Logged in.")
            time.sleep(1)
            break
        
        querry=listtasks()
        
        if querry==[]:
            print("No Tasks To Display.")
            
            try:
                input("Press Enter To Continue.")
                break
            
            except:
                print("\nReturning To Main Menu.")
                time.sleep(1)
                break
            
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][1]}")
            
        try:
            wtsk=input("Enter Which Activity you want to delete: ")
            wtsk=int(wtsk)
            
        except KeyboardInterrupt:
            print("Returning to main menu")
            time.sleep(0.4)
            break
            
        except ValueError:
            if wtsk == "q":
                print("Returning to Main Menu.")
                time.sleep(1)
                break
                
            print("Please enter a valid number.")
            time.sleep(1)
            continue

        except EOFError:
            print("No input was provided.")
            time.sleep(1)
            continue

        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Returning to Main Menu.")
            time.sleep(1)
            break

        except OSError:
            print("A system input/output error occurred.")
            print("Returning to Main Menu")
            time.sleep(1)
            break

                        
        if wtsk>len(querry) or wtsk<0:
            print("Wrong Input")
            time.sleep(1)
            continue
                    
        try:
            tskid=querry[wtsk-1][0]
            suretodelete=input("Are you sure you want to delete(y/N) ").lower()

        except ValueError:
            print("Please enter a valid input.")
            time.sleep(1)
            continue

        except EOFError:
            print("No input was provided.")
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Returning to Main Menu.")
            time.sleep(1)
            break

        except OSError:
            print("A system input/output error occurred.")
            print("Returning to Main Menu.")
            time.sleep(1)
            break
        
        if suretodelete=="y":
            querry=f"DELETE FROM tasks WHERE id=%s"
            data=(tskid,)
            response=db.DBSaveData(querry,data)
            input(response)
            if response["status"]==True:
                print("Task Deleted.")
                time.sleep(1)
                break
            else:
                print("Task Not Deleted. \nAn Error Occured")
                print(response["error"])
                input("Press 'enter' to continue.")
                break

if __name__=="__main__":
    deleteActivity()
