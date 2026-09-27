from newScreen import header
import variables as v
import database as db
import time
import categories as c



# Function to Update Activity
def updateActivity():
    if v.userVerified==False:
        print("Login First")
        exit()
    categories = c.listAllCategories("name_id")
    while True:
        header()
        querry="SELECT * FROM tasks where user_id=%s"
        data=(v.userID,)
        response=db.DBExecute(querry,data)
        if response==[]:
            print("No Tasks to Update")
            time.sleep(1)
            break

        for i in range(len(response)):
            print(f"{i+1}. {response[i][1]}   :   {categories[response[i][2]]}")
            
        try:
            wtsk=input("Enter Which Activity you want to modify: ")
            wtsk=int(wtsk)

        except ValueError:
            if wtsk == "q":
                print("Returning to main menu")
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
            print("Returning to main memu")
            time.sleep(1)
            break
        
        except OSError:
            print("A system input/output error occurred.")
            print("Returning to main menu")
            time.sleep(1)
            break
        
        if wtsk>len(response) or wtsk<0:
            print("Enter a valid whole number.")
            time.sleep(1)
            continue
            
        tskid=response[wtsk-1][0]
        todo=["Update Name","Update Category"]
        
        for i in range(len(todo)):
            print(f"{i+1}. {todo[i]}")
        try:
            whattochange=input("Enter what you want to change:")
            whattochange=int(whattochange)
            
        except ValueError:
            if whattochange=="q":
                print("Returning to main menu.")
                time.sleep(1)
                break
                
            print("Please enter a valid whole number.")
            continue
        
        except EOFError:
            print("No input was provided.")
            time.sleep(1)
            continue
        
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Returning to main menu")
            time.sleep(1)
            break
        
        except OSError:
            print("A system input/output error occurred.")
            print("Returning to main menu")
            time.sleep(1)

        if whattochange>len(todo):
            print("Invalid choice")
            time.sleep(1)
            continue
            
        if whattochange==1:
            try:
                newname=input("Enter New Name to set.\n: ")

            except EOFError:
                print("No input was provided.")
                time.sleep(1)
                continue

            except KeyboardInterrupt:
                print("\nInput cancelled by the user.")
                print("Returning to main menu")
                time.sleep(1)
                break

            except OSError:
                print("A system input/output error occurred.")
                print("Returning to main menu")
                time.sleep(1)
                break

            querry="UPDATE tasks SET taskName=%s WHERE id=%s"
            data=(newname,tskid)
            response=db.DBSaveData(querry,data)
            if response["status"]==True:
                print("Updated Successfully")
                time.sleep(1)
                break

            else:
                print("Error in updating data")
                print(response["error"])
                exit()

            

        elif whattochange==2:
        
            userChoice=c.chooseCategory()

            querry="UPDATE tasks SET category=%s WHERE id=%s"
            data=(userChoice,tskid)
            response=db.DBSaveData(querry,data)
            if response["status"]==True:
                print("Update Sucessful")
                time.sleep(1)
                break
                
            else:
                print("Error is updating data")
                print(response["error"])
                exit()
                break

        else:
            print("Error with input")
            time.sleep(2)
            break


if __name__=="__main__":
    updateActivity()
