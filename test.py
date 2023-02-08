
def f4(data):
    l = []
    prev = ""
    count = 0
    unit = ""
    state = False
    for i in range(len(data)):

        if data[i].isalnum() and state == True:
            val = unit.replace(" ","")
            if len(val) > 1:
                count+= len(val)
            state = False

        elif data[i] in "!;:,. ":
            unit+=data[i]
            state = True

    if len(unit.split()) > 1:
        count += len(unit.split())
    print(unit)
    print(count)

s = "apple.. . .   ."
f4(s)