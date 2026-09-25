from newScreen import header
from login import loginUser
from newUser import createUser
import time

# Checking is the user new or old via login and register
def initial():
    condition=True
    while condition:
        header()
        print("Enter Your Choice: ")
        try:
            first_choice=input("1. Login\n2. Register\n'e' to exit\n-->")
            first_choice=int(first_choice)
            if first_choice==1:
                return 1
                
            elif first_choice==2:
                return 2
                
            else:
                print("Wrong Input \nPress 'q' to exit.")
                time.sleep(1)
                continue
                
        except ValueError:
            if first_choice == "e":
                print("Exiting...")
                time.sleep(1)
                break
            print("Please enter valid input.")
            time.sleep(1)
            continue
            
        except EOFError:
            print("No input was provided.")
            time.sleep(1)
            continue
            
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Thanks for using the app. : First_Screen.py")
            time.sleep(1)
            break
            
        except OSError:
            print("A system input/output error occurred.")
            time.sleep(1)
            break

if __name__=="__main__":
    initial()

