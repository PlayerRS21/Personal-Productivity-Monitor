




    # Function to Update Activity
    def updateActivity(self):
        self.newScreen()
        # print(f"User:{self.userName}--------------Login at:{self.startTime}")
        if self.userVerified!=True:
            print("User Not Logged in.")
            time.sleep(1)
            self.loginUser()
            return
        querry=f"SELECT * FROM tasks WHERE created_by='{self.userName}'"
        self.cursor.execute(querry)
        querry=self.cursor.fetchall()
        if querry==[]:
            print("No Tasks To Display.")
            input("Press Enter To Continue.")
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][1]}   :   {querry[i][2]}")
        try:
            wtsk=input("Enter Which Activity you want to modify: ")
            wtsk=int(wtsk)
        except KeyboardInterrupt:
            print("Returning to main menu")
            time.sleep(0.4)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()
        except:
            if wtsk=="e":
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                # self.newScreen()
                self.whattodo()
            print("Wrong Input...")
            time.sleep(0.7)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.updateActivity()
        if wtsk>len(querry) or wtsk<0:
            print("Wrong Choice.")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.updateActivity()
        tskid=querry[wtsk-1][0]
        todo=["Update Name","Update Category"]
        for i in range(len(todo)):
            print(f"{i+1}. {todo[i]}")
        try:
            whattochange=int(input("Enter what you want to change:"))
        except:
            print("Incorrect Input")
            time.sleep(1)
            # os.system('cls' if os.name == 'nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.updateActivity()
        if whattochange==1:
            newname=input("Enter New Name to set.\n: ")
            querry=f"UPDATE tasks SET taskName='{newname}' WHERE id={tskid}"
            try:
                self.cursor.execute(querry)
                self.conn.commit()
                print("Done...")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                # self.newScreen()
                self.whattodo()
            except mysql.connector.Error as e:
                print("Error Occured:\n"+e)

        elif whattochange==2:
            # self.newScreen()
            print("Choose new category: ")
            # tsk=["Python","DSA","SQL","C++","Projects","Linux","Collage Work","Other"]
            for i in range(len(self.tsk)):
                print(f"{i+1}. {self.tsk[i]}")
            print()
            try:
                i=input("--> ")
                i=int(i)
            except KeyboardInterrupt:
                print("Returning to Main Menu")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.whattodo()
            except:
                if i=="e":
                    print("Returning to Main Menu")
                    time.sleep(1)
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    # print(self.__logo)
                    self.whattodo()
                print("Wront Choice.")
                time.sleep(1)
                self.updateActivity()
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
            if i>len(tsk):
                print("Incorrect Choice.")
                time.sleep(0.5)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                # self.addActivity()
                self.updateActivity()
            querry=f"UPDATE tasks SET category='{self.tsk[i-1]}' WHERE id={tskid}"
            try:
                self.cursor.execute(querry)
                self.conn.commit()
                print("Done...")
                time.sleep(1)
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print(self.__logo)
                self.whattodo()
            except mysql.connector.Error as e:
                print(e)
