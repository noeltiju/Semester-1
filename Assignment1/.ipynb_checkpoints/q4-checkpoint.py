from math import *

def formula(t): #Returns the value of the integrand
    val = 2000 * (log (140000 / (140000 - (2100 * t)))) - (9.8 * t)
    return val

dt = 0.25
start = a = int(input())
end = b = int(input())
area = 0
while a <= b: #Keeps adding dt to a until it reaches the end value
    area += abs(formula(a))
    a += dt

print(f"Area {area}")