contacts = {"name":[], "phone":[]}

contacts["name"] = ["Anna", "Jenifer", "Mik", "Ami"]
contacts["phone"] = ["+371 234567", "+372 98456", "+1 4567849", "+90 9874654"]

while True:
    menu_item = int(input("""What do you want? 
        1-print
        2-add
        3-remove
        4-exit\n"""))

    if menu_item == 1:
        print("----------\nYour phonebook")
        contacts_length = len(contacts["name"])
        for i in range(0, contacts_length):
            print("--------------------")
            print(f'Name: {contacts["name"][i]}; Phone: {contacts["phone"][i]}')

    elif menu_item == 2:
        print("Adding contact")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts["name"].append(name)
        contacts["phone"].append(phone)

    elif menu_item == 3:
        print("Removing contact")
        name = input("Enter name: ")        
        index = contacts["name"].index(name)
        contacts["name"].pop(index)
        contacts["phone"].pop(index)    

    elif menu_item == 4:
        exit()