a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite um último número: "))

# a é igual o b
if a == b:
    # verifica se b e a são iguais ao c
    if b == c:
        print(f"Não temos um maior pois todos os números são iguais: {a}")
    else:
        # Verifica se o a e b são maiores que o c
        if a > c:
            print(f"O primeiro e o segundo número são iguais e são os maiores: {a}")
        # Se o a e b que são iguais forem menores que c, exibe c como maior
        else:
            print(f"O {c} é o maior número")
# Se o a for diferente do b
else:
    # se o a for diferente do b mas igual ao c
    if a == c:
        # verifica se o a e c são maiores que o b
        if a > b:
            print(f"O primeiro e o último número são iguais e são os maiores: {a}")
        # se o a e o c forem menores, então o maior é o b
        else:
            print(f"O maior número é {b}")
    # se o A e o C forem diferentes um do outro
    else:
        # ver se o b é igual ao c
        if b == c:
            # ver se o b e c são maiores que o a
            if b > a:
                print(f"O segundo e o último número são iguais e são os maiores: {b}")
            # se o b e c forem menores que o a, então exibe a como maior
            else:
                print(f"O maior número é {a}")
        # se o b for diferente do c
        else:
            # ver se o a é maior que b
            if a > b:
                # se o a for maior que b, ver se é maior que c também
                if a > c:
                    print(f"O maior número é {a}")
                else:
                    print(f"O maior número é {c}")
            # se a for menor que b
            else:
                # ver se o b é maior que c
                if b > c:
                    print(f"O maior número é {b}")
                else:
                    print(f"O maior número é {c}")
