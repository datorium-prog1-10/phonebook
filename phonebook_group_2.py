contacts = {'name':[], 'phone':[]}
contacts["name"] = ['Anna', 'Jenifer', 'John', 'Mik']
contacts["phone"] = ['+371 123456789', '+372 456789', '+90 456798', '+1 123456789']

while True:
    menu_answer = input("""What do you want?
        1-print
        2-add
        3-remove
        4-exit\n""")

    menu_choice = int(menu_answer)
    if menu_choice == 1:
        print("Printing youe phonebook contacts:")
        contacts_length = len(contacts['name'])        
        for i in range(0, contacts_length):  
            print("------------------------------------")
            print(f"Name, Phone: {contacts['name'][i]}, {contacts['phone'][i]}")

    elif menu_choice == 2:
        print("Adding new contact")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts["name"].append(name)
        contacts["phone"].append(phone)
    elif menu_choice == 3:
        print("Removing a contact")
        name = input("Enter name: ")        
        index = contacts['name'].index(name)
        contacts['name'].pop(index)
        contacts['phone'].pop(index)
    elif menu_choice == 4:
        exit()
    