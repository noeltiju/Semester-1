
#This list is used to store the word of elements >= 20
tens_list = ["","","twenty","thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#This list is used to store the word of elements 1 <x< 9
ones_list = ["","one","two","three","four","five","six","seven","eight","nine"]

#This list is used to store the ans of elements 10 < x < 19
special_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"] 

#hundred_list = ["","one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
def ten_crore(n):
    global ans
    num = int(n)
    if n[0]!="1":
        ans = ans + tens_list[int(n[0])]+ " " + ones_list[int(n[1])] + " crore "

    else:
        ans = ans + special_list[int(n[1])] + " crore "

def crore(n):
    global ans
    num = int(n)
    if num!=0:
        ans = ans + ones_list[num] + " crore "

def ten_lac(n):
    global ans
    num = int(n)
    if n[0]!="1":
        ans = ans + tens_list[int(n[0])]+ " " + ones_list[int(n[1])] + " lac "

    else:
        ans = ans + special_list[int(n[1])] + " lac "

def lac(n):
    global ans
    num = int(n)
    if num!=0:
        ans = ans + ones_list[num] + " lac "

def ten_thousand(n):
    global ans
    num = int(n)
    if n[0]!="1":
        ans = ans + tens_list[int(n[0])]+ " " + ones_list[int(n[1])] + " thousand "

    else:
        ans = ans + special_list[int(n[1])] + " thousand "

def thousand(n):
    global ans
    num = int(n)
    if num!=0:
        ans = ans + ones_list[num] + " thousand "

def hundred(n):
    global ans
    num = int(n)
    if num!=0:
        ans = ans + ones_list[num] + " hundred "

def tens(n): 
    
    global ans
    num = int(n)
    ans = ans + tens_list[num] + " "

def ones(n):

    global ans
    num = int(n)
    ans = ans + ones_list[num]  + " "

def special(n):

    global ans
    num = int(n)
    ans = ans + special_list[num]

n = input()
ans = ""
i = -len(n)
while i <=-1:
    if i == -9:
        ten_crore(n[i:i+2])
        i+=2
    elif i == -8:
        crore(n[i])
    elif i == -7:
        ten_lac(n[i:i+2])
        i+=2
        continue

    elif i == -6:
        lac(n[i])
        
    elif i == -5:
        ten_thousand(n[i:i+2])
        i+=2
        continue

    elif i == -4:
        thousand(n[i])
    
    elif i == -3:
        hundred(n[i])

    elif i == -2:
        if n[i] == "1":
            special(n[-1])
            break

        else:
            tens(n[i])

    elif i == -1:
        ones(n[i])

    i+=1
print(ans)


    