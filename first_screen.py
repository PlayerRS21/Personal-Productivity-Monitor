from newScreen import header
from login import loginUser
from newUser import createUser

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
                # print("Triggering Login User Func.")
                # condition = False
                loginUser()
            elif first_choice==2:
                # print("Triggering Create user Func.")
                # condition = False
                createUser()
            else:
                print("Wrong Input \nPress 'q' to exit.")
                continue
        except ValueError:
            if first_choice == "e":
                print("Exiting...")
                break
            print("Please enter valid input.")
            continue
            
        except EOFError:
            print("No input was provided.")
            continue
            
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Thanks for using the app. : First_Screen.py")
            break
            
        except OSError:
            print("A system input/output error occurred.")
            break
    # print("Thanks For Using the App.  : First_Screen.py")

if __name__=="__main__":
    initial()

