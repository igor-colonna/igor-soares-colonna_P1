def nob(num_a,num_b):
    resposta = 0
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    if (num_a >= 1 and num_a <= 99) and (num_b >= 1 and num_b <= 99):
        a1 = num_a // 10
        b1 = num_b // 10
        a2 = num_a % 10
        b2 = num_b % 10
        resposta = a1 + b1 + a2 + b2
    else:
        print("Valor Inválido")
    return resposta

def main():
    print(nob(21,36))

main()
