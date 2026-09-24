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

# def defaultList(): 
    # return {"Python":"001","DSA":"002","SQL":"003","C++":"004","Projects":"005","Linux":"006","Collage Work":"007","Other":"008"}

