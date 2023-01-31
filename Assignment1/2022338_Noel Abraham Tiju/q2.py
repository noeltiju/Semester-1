x_max = 0 ; y_max = 0 #Initializing the chairs and tables initially to 0
max_profit = 0
M=10
def profit(x, y): #Checks if p > max_profit and changes respectively
    global max_profit , x_max , y_max
    if x > M and y > M:
        p = (90 * M) + (100 * (x-M))  + 25 * M + (30 * (y-M))
    elif x > M:
        p = (90 * M) + (100 * (x-M)) + 25 * y
    elif y > M:
        p = (90 * x) + (25 * M) + (30 * (y-M))
    else:
        p = 90*x + 40*y

    if p >= max_profit:
        max_profit = p
        x_max = x
        y_max = y

def labour_hours(x, y): #Checks if the constraint conditions are satisified
    if ((8 * x) + (2 * y) <= 400) and ((2 * x) + (y) <= 120):
        profit(x,y)


for x1 in range(0,61): #Iterates through maximum tables and chairs that can produced
    for x2 in range(0,201):
        labour_hours(x1,x2)


print(f"Optimum chairs to be produced {y_max}")
print(f"Optimum tables to be produced {x_max}")
print(f"Max profit is {max_profit}")