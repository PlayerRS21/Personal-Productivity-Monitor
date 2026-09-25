import os
import json


def defaultList():
    return {"101":"Python","102":"DSA","103":"SQL","104":"C++","105":"Projects","106":"Linux","107":"Collage Work","108":"Other"}

if not os.path.isfile(".categories.json"):
    with open(".categories.json","w") as file:
        json.dump(defaultList(),file,indent=4)

allCategories={}

with open(".categories.json","r")as file:
    allCategories=json.load(file)

def listAllCategories():
    return allCategories

def chooseCategory():
    while True:
        print("Select Category: \n")
        i=1
        for key in allCategories.values():
            print(f" {i}. {key}")
            i+=1
        
        try:
            selectCategory=input("--> ")
            selectCategory=int(selectCategory)
        
        except ValueError:
            if selectCategory=="e":
                print("Exiting...")
                time.sleep(1)
                condition=False
                break
        
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
        
        if selectCategory>len(allCategories):
            print("Incorrect Choice.")
            time.sleep(0.5)
            continue

        return selectCategory+100
