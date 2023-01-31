n = int(input())

for i in range(1,n): #Runs till second last line

    print("*"*i,end="")#Prints the left part

    print(" "* (2 * n - 1 - i - i),end="") # Prints the spaces in the middle

    print("*"*i,end="") #Prints the right part

    print()

print("*" * (2 * n - 1)) #Prints out the last line
