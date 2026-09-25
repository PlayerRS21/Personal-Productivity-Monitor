import newScreen as ns
import time
from datetime import datetime
import startTask as sa
import database as db
import variables as v
import router as r


# Function to login user
def loginUser():
    DataBase=db.connectDB()
    if DataBase[0]==True:
        conn=DataBase[1]
        cursor=DataBase[2]
    elif DataBase[0]==False:
        print("An Error Occured.")
        exit()
    qCount=0
    while qCount<2:
        ns.header()
        try:
            userName=input("Enter Your User Name or enter 'q' to quit: ")
            if userName=="q" and  qCount<1:
                qCount=qCount+1
                print("Can't use 'q' as user name.\nIf you want to quit press 'q' again.")
                time.sleep(1)
                continue
            elif qCount==1 and userName=="q":
                print("Exiting...")
                break
                
            passw=input("Enter Your Password: ")
            
        except ValueError:
            print("Please enter valid credentials.")
            continue
            
        except EOFError:
            print("No input was provided.")
            continue
        
        except KeyboardInterrupt:
            print("\nInput cancelled by the user.")
            print("Thanks for using the app.")
            break
        
        except OSError:
            print("A system input/output error occurred.")
            break

        query=f"SELECT * FROM users WHERE userName=%s"
        users=db.DBExecute(query,(userName,))
            
        if users==[]:
            print("Invalid Credentials.")
            time.sleep(2)
            continue
            
        if passw==users[0][3]:
            loginTime = time.strftime("%H:%M:%S",time.localtime(time.time()))
            querry=f"UPDATE users SET last_login=%s WHERE userName=%s"
            data=(str(datetime.now())[:10]+" "+str(loginTime),userName)
            
            response=db.DBSaveData(querry,data)
            if response["status"]==True:
                v.loginTime=loginTime
                v.userName=userName
                v.userVerified = True
                v.userID=users[0][0]
                print("Login Successful...")
                time.sleep(0.4)
                r.router()
                # print(v.userVerified,v.userID,v.loginTime,)
                
        else:
            print("Invalid Credentials. Try Again.")
            time.sleep(1)
            continue
if __name__=="__main__":
    loginUser()
