a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite um último número: "))

# a é igual ao b
if a == b:
    # verifica se b e a são iguais ao c
    if b == c:
        print(f"Não temos um menor pois todos os números são iguais: {a}")
    else:
        # Verifica se o a e b são menores que o c
        if a < c:
            print(f"O primeiro e o segundo número são iguais e são os menores: {a + 5}")
        # Se o a e b que são iguais forem maiores que c, exibe c como menor
        else:
            print(f"O {c + 5} é o menor número")
# Se o a for diferente do b
else:
    # se o a for diferente do b mas igual ao c
    if a == c:
        # verifica se o a e c são menores que o b
        if a < b:
            print(f"O primeiro e o último número são iguais e são os menores: {a + 5}")
        # se o a e o c forem maiores, então o menor é o b
        else:
            print(f"O menor número é {b + 5}")
    # se o A e o C forem diferentes um do outro
    else:
        # ver se o b é igual ao c
        if b == c:
            # ver se o b e c são menores que o a
            if b < a:
                print(f"O segundo e o último número são iguais e são os menores: {b + 5}")
            # se o b e c forem maiores que o a, então exibe a como menor
            else:
                print(f"O menor número é {a + 5}")
        # se o b for diferente do c
        else:
            # ver se o a é menor que b
            if a < b:
                # se o a for menor que b, ver se é menor que c também
                if a < c:
                    print(f"O menor número é {a + 5}")
                else:
                    print(f"O menor número é {c + 5}")
            # se a for maior que b
            else:
                # ver se o b é menor que c
                if b < c:
                    print(f"O menor número é {b + 5}")
                else:
                    print(f"O menor número é {c + 5}")
