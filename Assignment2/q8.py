urls = {}    
def reading():
    with open("q8_url.txt","r") as myfile:
        vals = myfile.read().splitlines()

    return vals

def main_function(element):
    l = element.split(", ")
    first = l[0]
    m = l[1].split(':')
    importance = float(m[0])
    urls_referred = list(set(l[2:])) ; length = len(urls_referred); imp = importance / length

    for i in urls_referred:
        if i in urls:
            urls[i]+=imp

        else:
            urls[i] = imp


vals = reading()
for i in vals:
    main_function(i)

values = list(set(urls.values()))
values.sort(reverse = True)
while True:
    n = int(input())
    if n > len(values):
        print("n is too large")
        continue
    else:
        break

for i in range(n):
    value = values[i]
    for i in urls:
        if urls[i] == value:
            print(i,end=" ")

    print(value)