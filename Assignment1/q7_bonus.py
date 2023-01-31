cost = int(input())
months = int(input())
allowance = 20000
rate = 0.5

for i in range(1,20001):
    saved_money = i
    month = 1
    while saved_money <= cost:
        interest = (saved_money * rate) /100 #Calculates interest and adds it 
        saved_money += interest
        month+=1 #Starts a new month
        saved_money += i

    if month == months:
        print(f"Savings fraction required is: {i / allowance}")
        break
