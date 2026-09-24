import time
from newScreen import header
import database as db


# Function to create new user
def createUser():
    errorOccured=False
    condition=True
    while condition:
        header()
        try:
            em=input("Enter Email: ")
            uName=input("Enter User Name: ")
            p=input("Enter Password or default will be 1234: ")
            
        except ValueError:
            print("Please enter valid credentials.")
            time.sleep(1)
            continue
        
        except EOFError:
            print("No input was provided.")
            time.sleep(1)
            continue
        
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Exiting")
            errorOccured=True
            break
        
        except OSError:
            print("A system input/output error occurred.")
            errorOccured=True
            break
            
        if p !="":
            data=(uName,em,p)
        elif p=="":
            data=(uName,em,"1234")
            
        response=db.addUserEntry(data)
        
        if response["status"]==True:
            print(f"User \"{uName}\" is created.")
            break
        else:
            print(response["error"])
            errorOccured=True
            break
    # if not errorOccured:
        # print("Thank You For Using The App : newUser.py")
    # else:
        # print("Try Again.")
