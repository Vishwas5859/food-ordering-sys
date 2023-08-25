# Here we are writing admin functionality()--

import json

class admin:
    def __init__(self):
        self.count = 0
        self.food_details = {}

    def admin_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "Admin" and password == "Admin":
            return "**************************Login Successfully********************************"
        else:
            return "Please give valid ID"
            
    def add_food(self):
        self.count += 1
        food_name = input("Enter the food name: ")
        food_quantity = input("Enter the food quantity: ")
        price = float(input("Enter the price of food: "))
        discount = int(input("Enter the discount the food: "))
        stock = int(input("Enter the stock of food: "))
        food_data = {"name":food_name,"quantity":food_quantity,"price":price,"discount":discount,"discounted_price":price - (((price)*discount)/100),"stock":stock} 
        self.food_details[self.count] = food_data
        with open("add_food.json","w") as f:
            json.dump(self.food_details,f,indent=4)
        return self.food_details   
    
    def edit_food(self):
        with open("add_food.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Food_ID : {k} || Food_Details : {v}") 

        id = input("Enter the food ID which you want to edit: ")
        fild = input("Enter the field in which you want to edit: ")
        update_value = input("Enter the updated value: ")
        data[id][fild] = update_value 

        with open("add_food.json","w") as f:
            json.dump(data,f,indent=4)
        return data

    def view_food(self):
        with open("add_food.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Food_ID : {k} || Food_Details : {v}") 
        return data 

    def remove_food(self):
        with open("add_food.json",'r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Food_ID : {k} || Food_Details : {v}")

        id = input("Enter the Id of food you want to remove: ")
        del data[id]
        with open("add_food.json","w") as f:
            json.dump(data,f,indent=4)
        return data   
   

x = admin()
# print(x.add_food())
# print(x.add_food())
# print(x.add_food())
# x.edit_food()