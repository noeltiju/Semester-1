def f4(d):
    unit = ""
    count = 0
    for i in d:
        if i in ",.:;" or i == " ":
            unit+=i

        elif i.isalpha() or i.isnumeric():
            l = unit.split()
            if len(l)>1:
                count+=len(l)
            unit = ""
    print(unit)
    l = unit.split()
    if len(l)>1:
        count+=len(l)
    print(count)

f4("Apple 1. . . ....  Mango . . . ")