n = int(input())
num_str = str(n)
length = len(num_str)
val = 0 #Variable indicating whether zero is a digit or no
ans = ""
#This list is used to store the word of elements >= 20
tens_list = ["","","twenty","thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#This list is used to store the word of elements 1 <x< 9
ones_list = ["","one","two","three","four","five","six","seven","eight","nine"]

#This list is used to store the ans of elements 10 < x < 19
special_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"] 
def tens(n): 
# Return the first part of the value of a two digit num

    global ans
    num = int(n)
    ans = ans + tens_list[num]
    if val:
        ans += " "

def ones(n):

# Return the second part of the value of a two digit num or 
# the ans of a one digit number

    global ans
    num = int(n)
    ans += ones_list[num]

def special(n):
# Returns ans for values between 10 and 19

    global ans
    num = int(n)
    ans += special_list[num]


if length == 2:
    if num_str[1] != "0":
        val = 1

    if num_str[0] == "1":
        special(num_str[1])

    else:
        tens(num_str[0])
        ones(num_str[1])

else:
    if n == 0:
        ans = "zero"

    else:
        ones(num_str[0])

print(ans)