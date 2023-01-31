def fac(n):
    fac = 1
    if n == 1 or n == 0:
        return fac

    for i in range(2, n+1):
        fac *= i

    return fac

def cos(x):
    n = 0
    ans = 0
    while n < 10:
        val = ((-1) ** n) * ((x ** (2 * n))/fac(2 * n))
        ans += val
        n+=1

    return ans

def sin(x):
    n = 0
    ans = 0
    while n < 10:
        val = ((-1) ** n) * ((x ** (2 * n + 1))/fac(2 * n + 1))
        ans += val
        n+=1

    return ans

def tan(x):
    return sin(x) / cos(x)

angle = float(input())
h = horizontal = float(input())

radians = (angle * 3.14) / 180

v = vertical =  tan(radians) * h #Forumula for finding height
l = length = h / cos(radians)    #Formula for finding hypoteneuse
if angle == 90:
    v = "Infinite"
    l = "Infinite"

print(f"Height of the pole: {v}")
print(f"Length of the pole: {l}")




