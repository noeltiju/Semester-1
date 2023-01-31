cost = int(input())
allowance = 20000
rate = 0.5
sf = 0.1
saved_money = sf * allowance
month = 1

while saved_money <= cost:
    interest = (saved_money * rate) /100 #Calculates interest and adds it 
    saved_money += interest
    month+=1 #Starts a new month
    saved_money += (sf * allowance)
     
print(f"Number of months: {month}")
print(f"Remaining saving: {saved_money-cost}")

#Bonus problem ******************************

