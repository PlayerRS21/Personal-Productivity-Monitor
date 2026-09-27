import database as db
import variables as v
import time

def listAllCategories(returntype:"name"|"id"|"name_id"):
    querry="SELECT category_id, category_name FROM categories"
    # data=(v.userID,)
    response = db.DBExecute(querry,tuple())
    # if response==[] and v.userID!="":
        # print("No category settings found")
        # print("Recreating new with default categories")
        # default=["Python","DSA","SQL","C++","Projects","Linux","Collage Work","Others"]
        # querry="INSERT INTO categories category_name VALUES (%s)"
        # for i in default:
            # data=(i,)
            # db.DBExecute(querry,data)
        
    # (category_id, category_name, user_id)
    if returntype=="name":
        lst=[]
        for i in range(len(response)):
            lst.append(response[i][1])
            
        return lst

    elif returntype=="id":
        lst=[]
        for i in range(len(response)):
            lst.append(response[i][0])

        return lst

    elif returntype=="name_id":
        lst={}
        for i in range(len(response)):
            lst[response[i][0]]=str(response[i][1])

        return lst

    else:
        lst=[]
        return lst


def chooseCategory():
    while True:
        print("Select Category or press 'q' to go back: \n")

        categories = listAllCategories("name_id")

        i=1
        keys=[]
        for key,value in categories.items():
            print(f"{i} {value}")
            keys.append(key)
            i=i+1
        
        try:
            selectCategory=input("--> ")
            selectCategory=int(selectCategory)
        
        except ValueError:
            if selectCategory=="q":
                print("Exiting...")
                time.sleep(1)
                condition=False
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
            print("Returning to main menu.")
            time.sleep(1)
            condition=False
            break
        
        except OSError:
            print("A system input/output error occurred.")
            condition =False
            break
        
        if selectCategory>len(categories):
            print("Incorrect Choice.")
            time.sleep(0.5)
            continue

        return keys[selectCategory-1]
        break

if __name__=="__main__":
    print(chooseCategory())
