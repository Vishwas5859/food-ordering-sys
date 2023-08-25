# here we are writing user functionality()--

import json
class user:
    def __init__(self):
        self.register_details = {}
        self.ordered_items = {}
        self.count = 0

    def register(self):
        full_name = input("Enter the full name: ")
        phone_number = input("Enter the phone number: ")
        self.email = input("Enter the Email ID: ")
        password = input("Enter the password: ")
        register_data = {"name":full_name,"phone_number":phone_number,"Email":self.email,"password":password}
        self.register_details[self.email] = register_data

        with open("personal_details.json","w") as f:
            json.dump(self.register_details,f,indent=4) 
        print("*******Registered Successfully*******")
        return self.register_details 
    


    def login(self):
        print("******Welcome to log in page********") 
        with open("personal_details.json","r") as f:
            data = json.load(f)

        while True:
            email = input("Enter the email_ID: ")
            key = input("Enter the password: ")
            if email in data:
                if key==data[email]["password"]:
                    print("***log in is successful***")
                    break
                else:
                    print("Please give valid details!")
            else:
                print("Please give valid details!")      

    def place_new_order(self):
        self.count = self.count+1
        self.ordered_food_list = []
        list_of_food = [{"name":"Tandoori chicken","Qty":"4 pieces","price":240},
                        {"name":"vegan burger","Qty":"1 piece","price":320},
                        {"name":"Truffle cake","Qty":"1 pieces","price":900}]
        
        print("Here is the menu")
        for i in list_of_food:
            print(i)

        user_input = int(input("Select the food item with you want to order : "))
        if user_input == 0:
            self.ordered_food_list.append(list_of_food[0])

        elif user_input == 1:
            self.ordered_food_list.append(list_of_food[1])

        elif user_input == 2:
            self.ordered_food_list.append(list_of_food[2])

        else:
            print("choose the oder from menu!") 

        print("Press 1 for order confirmation")
        print("Press 2 for oder deletion")
        option = int(input("Enter the choice: "))
        self.ordered_items[self.count] = self.ordered_food_list
        
        if option ==1:
            print("oder placed successfully")
            with open("order_history.json","w") as f:
                json.dump(self.ordered_items,f,indent=4)
        else:
            print("Order cancelled!")
        return self.ordered_food_list      


    def order_history(self):
        for k,v in self.ordered_items.items():
            print(f"order_ID : {k} || order_details : {v}")


    def update_profile(self):
        with open("personal_details.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Email_ID : {k} || Personal_details : {v}")

        email_id = input("Enter email ID to update: ")
        field = input("Enter the filed to be updated: ")
        updated_value = input("Enter the updated value: ")
        data[email_id][field] = updated_value

        with open("personal_details.json","w") as f:
            json.dump(data,f,indent=4) 
        print("*******Updated Successfully*******")
        return data                 

            
x = user()
# print(x.register())
# print(x.register())
#(x.login())
# print(x.place_new_order())
# print(x.place_new_order())
# print(x.order_history())

# print(x.update_profile())


