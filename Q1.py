def segundograu(a,b,c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        return 0
    else:
        return 1

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
segundograu(a,b,c)