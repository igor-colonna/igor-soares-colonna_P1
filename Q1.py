def segundograu(a,b,c):
    delta = (b**2) - (4*a*c)
    x1 = ((-b) + (delta**0.5))/(2*a)
    x2 = ((-b) - (delta**0.5))/(2*a)
    print("As raízes são: ",x1,x2)
    if delta < 0:
        return 0
    else:
        return 1

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print(segundograu(a,b,c))