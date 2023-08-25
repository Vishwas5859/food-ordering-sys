import sys
from admin1 import *

admin_interface = admin()


print("Please login")
print(admin_interface.admin_login())

while True:
    print("Press 1 for add food")
    print("Press 2 for edit food")
    print("Press 3 for view food details")
    print("Press 4 for remove food")
    print("Press 5 for exit ")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        print(admin_interface.add_food())
        print("*************food added successfully**************")

    elif option == 2:
        print(admin_interface.edit_food())
        print("*************food edited successfully**************")

    elif option == 3:
        print(admin_interface.view_food())
        print("*************view successfully**************")

    elif option == 4:
        print(admin_interface.remove_food())
        print("*************food added successfully**************")

    if option == 5:
        print("*************Thank you for using our application**************")
        sys.exit()
    
    else:
        print("Provide correct option!")

    
        

    
