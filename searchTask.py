from newScreen import header
import time
import categories as c
import database as db
import variables as v

def loginCheck():
    if v.userVerified == False:
        print("Login First")
        exit()

# Function to Search Tasks
def searchActivity():
    loginCheck()
    while True:
        header()
        try:
            tasknameInput=input("Search via name: ")
            querry="SELECT taskName,category,user_Id FROM tasks WHERE (taskName LIKE CONCAT('%',%s,'%') OR taskName LIKE CONCAT('%',%s,'%')) AND user_Id = %s"

        except ValueError:
            print("Please enter a valid whole number.")
            time.sleep(1)
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
            break
            
        data=(tasknameInput,tasknameInput.lower(),v.userID)
        response=db.DBExecute(querry,data)
        
        if response == []:
            try:
                userChoiceToCheckViaCategory=input("No Results Found want to search via category? (Y/n) ")

            except ValueError:
                print("Please enter a valid whole number.")
                time.sleep(1)
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
                break

        # else:
            # for i in range(len(response)):
                # print(f"{i+1}. {response[i][0]}  {c.allCategories[str(response[i][1])]}")

            # try:
                # input("Press enter to continue.")

            # except:
                # break
                
            if userChoiceToCheckViaCategory.lower()=="y" or userChoiceToCheckViaCategory.lower()=="":
                userChoice=c.chooseCategory()
                querry=f"SELECT taskName,category FROM tasks WHERE category=%s AND user_Id =%s"
                data=(userChoice,v.userID)
                response =db.DBExecute(querry,data)
            
                if response ==[]:
                    print("No Record Found Try Again With Different Filters...")
                    time.sleep(2)
                    break
                    
                for i in range(len(response)):
                    print(f"{i+1}. {response[i][0]}    :    {response[i][1]}")
                    try:
                        input("Press Enter To Continue. ")
                        break
    
                    except:
                        print("Returning to main menu")
                        time.sleep(1)
                        break

        else:
            for i in range(len(response)):
                print(f"{i+1}. {response[i][0]}  {c.allCategories[str(response[i][1])]}")
            try:
                input("Press enter to continue.")

            except:
                print("Returning...")
                time.sleep(0.7)
                break
