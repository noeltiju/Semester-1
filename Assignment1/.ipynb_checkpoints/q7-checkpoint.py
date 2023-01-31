cost = int(input())
allowance = 20000
rate = 0.5
sf = 0.1
saved_money = sf * allowance
month = 1

while saved_money <= cost:
    interest = (saved_money * rate) / 100
    saved_money+=interest
    month+=1
    saved_money += (sf * allowance)
    
print(month)
