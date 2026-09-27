import first_screen as fs
from login import loginUser
from newUser import createUser
import variables as v

function=fs.initial()
while True:
    if function == 1:
        import router 
        loginUser()
        break

    elif function == 2:
        import router 
        createUser()
        break

    else:
        print(function)
        print("Something Went Wrong")
        exit()
