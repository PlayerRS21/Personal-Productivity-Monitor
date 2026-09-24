






    # Function to Search Tasks
    def searchActivity(self):
        self.newScreen()
        # print(f"User:{self.userName}--------------Login at:{self.startTime}")
        i=input("Search via name: ")
        try:
            querry=f"SELECT taskName,category,created_by FROM tasks WHERE (taskname LIKE '%{i}' OR taskName LIKE '{i}%' OR taskName LIKE '%{i}%' OR taskName LIKE '%{i.lower()}' OR taskName LIKE '{i.lower()}%' OR taskName LIKE '%{i.lower()}%') AND created_by ='{self.userName}'"
            self.cursor.execute(querry)
            querry=self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
            exit()
        if querry == []:
            print("No Results Found want to search via category? (Y/n) ")
            x=input()
            if x.lower()=="y" or x.lower()=="":
                for i in range(len(self.tsk)):
                    print(f"{i}. {self.tsk[i]}")
            x=input("Choose Category: ")
            try:
                x=int(x)
            except:
                print("Wrong Input.")
                time.sleep(0.7)
                # os.system('cls' if os.name=='nt' else 'clear')
                # print(self.__logo)
                # self.newScreen()
                self.searchActivity()

            if x>len(self.tsk) or x<0:
                print("Wrong Input.")
                time.sleep(0.7)
                search(querry)
                querry=f"SELECT (taskName,category,created_by) FROM tasks WHERE category='{self.tsk[x-1]}' AND created_by ='{self.userName}'"
                self.cursor.execute(querry)
                querry=self.cursor.fetchall()
        if querry ==[]:
            print("No Record Found Try Again With Different Filters...")
            time.sleep(2)
            # os.system('cls' if os.name=='nt' else 'clear')
            # print(self.__logo)
            # self.newScreen()
            self.whattodo()
        for i in range(len(querry)):
            print(f"{i+1}. {querry[i][0]}    :     {querry[i][1]}")
        input("Press Enter To Continue. ")
        # os.system('cls' if os.name=='nt' else 'clear')
        # print(self.__logo)
        # self.newScreen()
        self.whattodo()
