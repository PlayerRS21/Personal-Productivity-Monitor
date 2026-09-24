import variables as v
# import login as lin
import os

# Displaying Header
def header():
    os.system('cls' if os.name=='nt' else 'clear')
    print(v.logo)
    if v.userVerified==True:
        print(f"User: {v.userName}-------------------Login at:{v.loginTime}")
        print()
