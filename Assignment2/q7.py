address_book = {}
def reading(l):
    for i in l:
        vals = i.split(",")
        k = vals[0].split(":")
        name = k[1].title()
        
        if name not in address_book:
            d = {}
            for j in vals[1::]:
                k = j.split(":")
                d[k[0]] = k[1].title()

            address_book[name] = d
        else:
            if type(address_book[name]) == list:
                d = {}
                for j in vals[1::]:
                    k = j.split(":")
                    d[k[0]] = k[1].title()

                address_book[name].append(d)

            else:
                d1 = address_book[name]
                d2 = {}
                for j in vals[1::]:
                    k = j.split(":")
                    d2[k[0]] = k[1].title()

                address_book[name] = [d1,d2]

def writing(address_book):
    with open("q7_dictionary.txt",'w') as myfile:
        for name in address_book:
            value = address_book[name]
            if type(value) != list:
                address = value["address"] ; phone = value["phone"] ; email = value["email"]
                s = f"name:{name},address:{address},phone:{phone},email:{email}\n"
                myfile.write(s)

            else:
                for i in value:
                    address = i["address"] ; phone = i["phone"] ; email = i["email"]
                    s = f"name:{name},address:{address},phone:{phone},email:{email}\n"
                    myfile.write(s)

with open("q7_dictionary.txt","r") as myfile:
    value = myfile.read()
    if value == "":
        pass

    else:
        reading(value.splitlines())

while True:
    print("""
1. insert a new entry
2. delete an entry
3. find all matching entries given a partial name
4. find the entry with a phone number or email
5. exit
    """)

    command = int(input())

    if command == 5:
        break

    elif command == 1:
        name = input("Enter name: ").title()
        address = input("Enter address: ").title()
        phone = input("Enter phone: ").title()
        email = input("Enter email: ").title()

        if name in list(address_book.keys()):
            value = address_book[name]
            if type(value) == list:
                val = {"address": address , "phone": phone, "email": email}
                value.append(val)

            else:
                current_val = value
                val = {"address": address , "phone": phone, "email": email}
                address_book[name] = [current_val, val]

        else:

            val = {"address": address , "phone": phone, "email": email}
            address_book[name] = val
    
    elif command == 2:
        print(address_book)
        name = input("Enter name of address to delete: ").title()
        if name in address_book:
            address_book.pop(name)

    elif command == 3:
        partial = input().lower()
        found = 0
        for item in list(address_book.keys()):
            if partial in item.lower():
                value = address_book[item]
                found = 1
                if type(value) != list:
                    print(f'{item}, address: {value["address"]} phone: {value["phone"]} email: {value["email"]} ')
                
                else:
                    for val in value:
                        print(f'{item}, address: {val["address"]} phone: {val["phone"]} email: {val["email"]} ')

            

        if found == 0:
            print("Not found")

    elif command == 4:
        print("""
    find an entry: 

    1. using phone no
    2. using email

        """)

        option = int(input())
        ans = input().lower()

        for item in list(address_book.keys()):
            value = address_book[item]
            if type(value) != list:
                if option == 1:
                    if value["phone"].lower() == ans:
                        print(f'\n{item}, address: {value["address"]} phone: {value["phone"]} email: {value["email"]} ')
                        break
                elif option == 2:
                    if value["email"].lower() == ans:
                        print(f'\n{item}, address: {value["address"]} phone: {value["phone"]} email: {value["email"]} ')
                        break

            else:
                for val in value:
                    if option == 1:
                        if val["phone"].lower() == ans:
                            print(f'\n{item}, address: {val["address"]} phone: {val["phone"]} email: {val["email"]} ')
                            break
                
                    elif option == 2:
                        if val["email"].lower() == ans:
                            print(f'\n{item}, address: {val["address"]} phone: {val["phone"]} email: {val["email"]} ')
                            break

writing(address_book)