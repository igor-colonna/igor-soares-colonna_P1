def calcpi():
    result = 0
    n = 1
    while (-(1/n+2) + (1/n+4)) >= abs(5*(10**-8)):
        result += (-(1/n+2) + (1/n+4))
        n += 5
    pi = 4 * (1-result)
    return pi