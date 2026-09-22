import newScreen as ns
import mysql.connector
from mysql.connector import Error
import time
from datetime import datetime
from database import connectDB, dbExecute


# Function to login user
def loginUser():
    qCount=0
    while qCount<2:
        ns.header()
        try:
            userName=input("Enter Your User Name: ")
            if userName=="q" and  qCount<1:
                qCount=qCount+1
                print("Can't use 'q' as user name.\nIf you want to quit press 'q' again.")
                time.sleep(2)
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

        try:
            query=f"SELECT * FROM users WHERE userName=%s"
            # cursor.execute(query,(userName,))
            users=dbExecute(query,(userName,))
            # print(users)
            
        except mysql.connector.Error as e:
            print(f"Error in DataBase\n{e}")
            break
            
        if users==[]:
            print("Invalid Credentials.")
            time.sleep(2)
            continue
            
        if passw==users[0][3]:
            userVerified = True
            userName=userName
            startTime = time.strftime("%H:%M:%S",time.localtime(time.time()))
            sTimeHum=str(startTime)
            t=f"{str(datetime.now())[:10]} {sTimeHum[:2]}:{sTimeHum[3:5]}:{sTimeHum[6:8]}"
            querry=f"UPDATE users SET last_login='{t}' WHERE userName='{userName}'"
            
            try:
                cursor.execute(querry)
                conn.commit()
                print("Login Successful...")
                time.sleep(0.4)
                break
                
            except mysql.connector.Error as e:
                print(e)
                break
                
        else:
            print("Invalid Credentials. Try Again.")
            time.sleep(1)
            continue

db=connectDB()
if db[0]==True:
    conn=db[1]
    cursor=db[2]
    loginUser()
