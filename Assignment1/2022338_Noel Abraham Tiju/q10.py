#polynomial = x**3 - 10.5*x**2 + 34.5*x - 35
d_coeffs = [] #List of differential coeffs

def value(x):
    #Returns the value of the function
    return (x ** 3) - (10.5 * (x ** 2)) + (34.5 * x) - 35

    
def differentiate(x):
    #Returns the differential value of the function
    global d
    a = d_coeffs[0]
    b = d_coeffs[1]
    c = d_coeffs[2]

    return (a * (x ** 2)) + (b * x) + c

a = 1 ; b = -10.5 ; c = 34.5 ; d = -35 #Coeffs are decided here
d_coeffs.extend([3 * a, 2 * b, c]) #Differential coeffs are added
x0 = float(input())

while True:
    if value(x0) != 0:
        x = x0 - (value(x0) / differentiate(x0))
        x0 = x


    else:
        break    

print(f"The value reaches minimum at {x0} ")
print(f"The value is {value(x0)}")        


