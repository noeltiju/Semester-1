l = []
while True:
    val = input()
    if val == "":
        break

    k = list(map(float, val.split()))
    l.append(k)

matrix = []
for coordinate in l:
    matrix.append([coordinate[0],coordinate[1],1])
print("*****")
cx,cy = list(map(int, input().split()))
for i in range(len(matrix)):
    row = matrix[i]
    row[0] *= cx
    row[1] *= cy
    row[2] *= 1

print("*****\n")
for i in matrix:
    k = list(map(str,i))
    print(' '.join(k[0:-1]))

