from newScreen import header
import variables as v
import database as db
import time
import categories as c



def listtasks():
    querry=f"SELECT * FROM tasks WHERE user_id=%s"
    data=(v.userID,)
    return db.DBExecute(querry,data)

# Function to View Tasks Done
def viewActivity():
    while True:
        header()
        if v.userVerified!=True:
            print("Login First...")
            time.sleep(1)
            break
            
        querry=f"SELECT * FROM tasks WHERE user_id=%s"
        # data=(v.userID)
        data=(1000,)
        response=db.DBExecute(querry,data)
        
        if response!=[]:
        
            for i in range(len(response)):
                hours, remainder = divmod(response[i][5], 3600)
                minutes, seconds = divmod(remainder, 60)
                if minutes==0:
                    print(f"{i+1}. {response[i][1]} : {c.allCategories[str(response[i][2])]} :  {seconds}s")
                elif hours==0:
                    print(f"{i+1}. {response[i][1]} : {c.allCategories[str(response[i][2])]} :  {minutes}m {seconds}s")
                else:
                    print(f"{i+1}. {response[i][1]} : {c.allCategories[str(response[i][2])]} :  {hours}h {minutes}m {seconds}s")

            try:
                input("Press 'enter' to go back")
                break
                
            except KeyboardInterrupt:
                print("Returning to main menu.")
                time.sleep(1)
                break
            
            except OSError:
                print("A system input/output error occurred.")
                time.sleep(1)
                break
            except:
                pass
            
        else:
            input("No tasks done yet.\nPress 'Enter' to continue.")
            break

if __name__=="__main__":
    viewActivity()
