from newScreen import header
import variables as v
from datetime import datetime
import database as db
from viewTask import listtasks




def viewStatDaily():
    query="SELECT * FROM tasks WHERE user_ID=%s AND category=%s AND created_on >= CURDATE()  AND created_on <= NOW()"
    # print(listtasks()[0][4],"    :     ",datetime.now())
    data=("1000","108")
    
    response = db.DBExecute(query,data)
    print(response)
    print(f"Total {len(response)} Entries")
    
    # 2026-09-23 11:13:47     :      2026-09-23 22:57:15.950894
    
    # data=("1000","108")
    


def viewStatMonthly():
    pass

# Fubction to View Statistics
def viewStat():
    while True:
        header()
        
        querry=f"SELECT SUM(total_time) FROM tasks WHERE created_by=%s AND category=%s"
        print(" Total Productivity ")
        print("-"*32)
        th,tm,ts=0,0,0
        for i in range(len(self.tsk)):
            data=(self.userName,self.tsk[i])
            self.cursor.execute(querry,data)
            lst=self.cursor.fetchone()
            if lst[0]!=None:
                print(f"{self.tsk[i]}:"," "*(30-8-(len(self.tsk[i]))),end="")
                lst=lst[0]
                lst=str(lst)
                lst=lst[-6:]
                # print(lst)
                h , m , s = [lst[i:i+2] for i in range(0, len(lst), 2)]
                th=th+int(h)
                tm=tm+int(m)
                ts=ts+int(s)
                print(f"{h}h {m}m")
        print("-"*32)
        while ts>60:
            ts=ts-60
            tm=tm+1
        while tm>60:
            tm=tm-60
            th=th+1
        print("Total"," "*(30-6-8),f"{th}h {tm}m {ts}s")

if __name__=="__main__":
    viewStatDaily()
