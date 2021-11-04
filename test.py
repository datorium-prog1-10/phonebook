contacts = {'name':[], 'phone':[]}
contacts["name"] = ['W41K3R ##0', 'W41K3R #71391', 'John', 'Anna']
contacts["phone"] = ['+371 123066789', '+372 456789', '+90 456798', '+1 1234051789']
while True:
    menu_answer = input(""""What do you want?
    1-print
    2-add
    3-remove
    4-exit\n""")
    menu_choice = int(menu_answer)
    if menu_choice == 1:
        print("PRINTING YOUR PHONEBOOK CONTACTS:")
        contacts_length = len(contacts['name'])
        for i in range(0, contacts_length):
            print("__________________________________________________________________")
            print(f"name:{contacts['name'][i]}\n{contacts['phone'][i]}")
    if menu_choice == 1:
        print(contacts)
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