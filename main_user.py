import sys
from user import *
userinterface = user()

while True:
    print("Press 1 for new register")
    print("press 2 for place new order")
    print("Press 3 for order history")
    print("Press 4 for update profile")
    print("Press 5 for Exit")

    option = int(input("Enter your choice: "))

    if option ==1:
        print(userinterface.register())
        print("Register Successfully")

    elif option == 2:
        print(userinterface.place_new_order())
        print("*"*100)

    elif option == 3:
        print(userinterface.order_history())
        print("*"*100)

    elif option == 4:
        print(userinterface.update_profile())

    elif option == 5:
        print("***********Thank You for using our Application**************")
        sys.exit()    

    else:
        print("Give proper input")



