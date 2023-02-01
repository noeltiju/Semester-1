val = int(input())
c = "* "
def upper_half(n):
    characters = c * n
    spaces = '  '*(2*(val-n))
    if n > 1:
        print(characters + spaces + characters)
        return upper_half(n-1)

    else:
        return characters + spaces + characters

i = 2
def lower_half(n):
    global i
    if i > n:
        return ""

    characters = c * i
    spaces = '  '*(2*(n - i))
    print(characters + spaces + characters)
    i+=1
    return lower_half(n)

print(upper_half(val))
print(lower_half(val))