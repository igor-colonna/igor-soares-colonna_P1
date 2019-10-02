def calcpi():
    dif = 1
    pi = 0
    x = 1
    y = 1
    while dif > (5*10**(-8)):
        piant = pi
        pi = pi + 4/(x*y)
        x += 2
        y *= -1
        dif = (piant - pi) * y
    print(pi)
calcpi()