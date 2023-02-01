menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
#Menu is stored in the list menu

def compute(orders):
    #Function computes the bill for a certain orders list
    bill = 0
    total_quantity = 0
    for i in orders:
        bill += i[2] * i[1]
        total_quantity += i[1]
        print(f"{i[0]}, {i[1]}, {i[2]*i[1]}Rs")

    print(f"TOTAL, {total_quantity} items, Rs{bill}")



while True:
    order = input().lower() #Command issued from the user

    if order == "show":
        count = 1
        for item in menu:
            print(f"{count}. {item[0]}   {item[1]}Rs")
            count+=1

    elif order == "order":
        orders = [] 
        while True:
            user_input = input()
            if user_input == "": #Empty input is used to terminate the loop
                break
            
            user_list = list(user_input.split())
            item_no = int(user_list[0])-1
            quantity = int(user_list[1])

            if item_no not in range(0,len(menu)+1): #If item no is out of index loop is skipped
                print("Item no not available")
                continue

            item = menu[item_no]
            price = item[1];name = item[0]
            orders.append([name,quantity,price])

        compute(orders)

    else:
        break