import first_screen 
from login import loginUser
from newUser import createUser
import router 
import variables as v

function=first_screen.initial()
while True:
    if function == 1:
        loginUser()
        break

    elif function == 2:
        createUser()
        break

    else:
        print("Something Went Wrong")
        exit()
