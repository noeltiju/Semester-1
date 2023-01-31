from math import log, exp

start = float(input())

def demand(p): 
    #Calculates log D(p)
    a = 10 ; b = 1.05
    return a - (b * p)

def supply(p): 
    #Calculates log S(p)
    c = 1 ; d = 1.06
    return c + (d * p)

while start < 10000: 
    #Creates its range and checks for equilibrium
    if demand(start) > supply(start):
        print(f"Equilibrium has reached at price: {start}")
        break

    start = 1.05*start

else:
    print("No equilibium found in this range")