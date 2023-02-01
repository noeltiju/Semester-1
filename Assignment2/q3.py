def yearbook_maker(yearbook):
    l = []
    with open("yearbook_q3.txt","r") as myfile:
        l = myfile.readlines()
    
    name = l[0][:len(l[0])-2]
    d={}

        
    for i in range(1,len(l)):
        item = l[i].strip()
        if ":" in item:
            yearbook[name] = d
            name = item[:len(item)-1]
            d={}

        else:
            k=item.split(", ")
            if len(k) > 1:
                d[k[0]] = int(k[1][-1])

    yearbook[name] = d

yearbook = {}
yearbook_maker(yearbook)
names = dict.fromkeys(list(yearbook.keys()),0)

for i in yearbook.keys():
    val = yearbook[i]
    count = 0
    for j in val.values():
        count+=j

    names[i] = count

max_val = max(names.values())
min_val = min(names.values())

print("Maximum signatures by: ")
for name in names:
    if names[name] == max_val:
        print(name,max_val)

print("\nMinimum signatures by: ")
for name in names:
    if names[name] == min_val:
        print(name, min_val)

