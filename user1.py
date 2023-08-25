import json 

class user1:
    def __init__(self):
        self.registraion_details = {}
        self.placed_orders = {}
        self.count = 0

    def registration(self):
        name = input("Enter the name: ")
        Ph_no = input("Enter the contact no: ")
        self.emial_id = input("Enter the Email ID: ")
        address = input("Enter the Address: ")
        password = input("Enter the password: ")
        registration_data = {"name":name,"ph_no":Ph_no,"email_id":self.emial_id,"address":address,"password":password}
        self.registraion_details[self.emial_id] = registration_data

        with open("add_register.json","w") as f:
            json.dump(self.registraion_details,f,indent=4)
        print("-------------------Registerd successfully---------------------")
        return self.registraion_details

    
    def login(self):
        with open("registraion_details.json",'r') as f:
            data = json.load(f)
        while True:
            email = input("Enter the Email ID: ")   
            key = input("Enter the password: ") 
            if email in data:
                if key == data[email]["password"]:
                    print("Login successful")
                else:
                    print("Provide vaild details")
            else:
                print("Provide vaild details")   
            return data         


    def place_order(self):
        self.count = self.count+1
        print("------------Welcome-------------")
        self.food_menu_list = []
        food_menu = [{"name":"Tandoori chicken","Qty":"4 pcs","price":"250"},
                     {"name":"Vegan burger","Qty":"1 pcs","price":"200"},    
                    {"name":"Truffle cake","Qty":"1 pcs","price":"750"}]

        for i in food_menu:
            print(i)

        print("Press 0 for Tandoori chicken")
        print("Press 1 for vegan burger")
        print("Press 2 for truffle cake")

        user_input = int(input("Enter your food: "))

        if user_input ==0:
            self.food_menu_list.append([food_menu[0]]) 

        elif user_input ==1:
            self.food_menu_list.append([food_menu[1]]) 

        elif user_input ==2:
            self.food_menu_list.append([food_menu[2]])  

        print("Press 1 for oder confirmation ")
        print("Press 2 for order cancellation")
        option = int(input("Enter your option : "))

        self.placed_orders[self.count] = self.food_menu_list

        if option ==1:
            print("Order palced successfully")
            with open("order_history1.json","w") as f:
                json.dump(self.placed_orders,f,indent=4)
        else:
            print("Order cancelled!")
        return self.food_menu_list 
    
    def order_history(self):
        for k,v in self.placed_orders():
            print(f"Order ID {k} || Order Details {v}")


















