import math
x0 = 5.0 #Initializing the values
y0 = 5.0
x = x0 ; y = y0
total_distance = 0

while True:
    distance = d = float(input())

    if (0 < d <= 25): #North condition
        y += d 
        total_distance += d

    elif (26 <= d <= 50): #South condition
        y -= d
        total_distance += d

    elif (51 <= d <= 75): #East condition
        x += d
        total_distance += d

    elif (d >= 76): #West condition
        x -= d 
        total_distance += d
    
    elif (d <= 0):
        break

print(f"Final coordinates are ({x}, {y})")
print(f"Total distance travelled is {total_distance}")
val = math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2))
print(f"The final straight line distance is {val}")
