population = [50, 1450, 1400, 1700, 1500, 600, 1200]
growth = 2.5
count = 0


def sum_population():
    sum = 0
    j = 0
    for i in population:
        sum += find_population(j,i)
        j+=1

    return sum

def find_population(no,pop):
    rate = growth - (0.4) * (no)

    for i in range(count):
        pop += (pop * rate) / 100
        rate -= 0.1

    return pop

max_population = sum_population()
while True:
    pop = sum_population()
    if pop >= max_population:
        max_population = pop
        count+=1


    else:
        break

print(f"Max population is: {max_population * 10 ** 6}")
print(f"Max population in: {count-1} years")