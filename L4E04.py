a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite um último número: "))

# Cenário q todos são iguais
if a == b:
    if b == c:
        print(f"Não temos um maior, todos os números são iguais: {a}")
    else:
        # Se a e b são iguais, mas o c é diferente
        if a > c:
            # a e b maior que c
            print(f"O primeiro e o segundo número são iguais e maiores: {a}")
        else:
            # c é maior que a e b
                print(f"O maior número é {c}")
    # a diferente do b
else:
    # a e c são iguais
    if a == c:
        # verificar se o a e c são maiores que b
        if a > b:
            print(f"O primeiro e o último número são iguais e maiores: {a}")
        else:
            # b maior que o a e c
                print(f"O maior número é {b}")
        # a diferente do c e diferente do b
    else:
        # b igual o c?
        if b == c:
            # se b == c então veja se eles são maiores que o a
            if b > a:
                print(f"O segundo e o último número são iguais e maiores: {b}")
            else:
                print(f"O maior número é {a}")
        # Se não existir empates (todos diferentes)
        else:
            # Ver se a é maior que b
            if a > b:
                # Sim, a é maior que b, agora veja se é maior que c
                if a > c:
                    # a > b e a > c
                    print(f"O maior número é {a}")
                else:
                    # a > b mas a < c
                    print(f"O maior número é {c}")
            else:
                # b > a, veja se o b é maior que o c também
                if b > c:
                    print(f"O maior número é {b}")
                # b > a mas b < c
                else:
                        print(f"O maior número é {c}")
