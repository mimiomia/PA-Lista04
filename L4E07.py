a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite um último número: "))

# Se todos os números forem iguais
if a == b:
    if b == c:
        print(f"Todos os números são iguais: {a}")
    else:
        # Verifica se o a e o b são menores que o c
        if a < c:
            print(f"A ordem crescente é: {a}, {b}, {c}")
        # Se o a e b que são iguais forem maiores que c, exibe c como o menor
        else:
            print(f"A ordem crescente é: {c}, {a}, {b}")
# Se o a for diferente do b
else:
    # Se o a for igual ao c
    if a == c:
        # Se a e c são menores que o b
        if a < b:
            print(f"A ordem crescente é: {a}, {c}, {b}")
        # Se a e c forem maiores, então o menor é o b
        else:
            print(f"A ordem crescente é: {b}, {a}, {c}")
    # Se o A e o C forem diferentes um do outro
    else:
        # Se o b é igual ao c
        if b == c:
            # Se o b e c são menores que o a
            if b < a:
                print(f"A ordem crescente é: {b}, {c}, {a}")
            # Se o b e c forem maiores que o a, então exibe a como o menor
            else:
                print(f"A ordem crescente é: {a}, {b}, {c}")
        # Se o b for diferente do c
        else:
            # Verifica qual é o menor
            if a < b:
                # Verifica se o a é menor que o c
                if a < c:
                    # Verifica qual é o segundo e qual é o maior
                    if b < c:
                        print(f"A ordem crescente é: {a}, {b}, {c}")
                    else:
                        print(f"A ordem crescente é: {a}, {c}, {b}")
                # Se o a não for menor que o c, então c é o menor
                else:
                    print(f"A ordem crescente é: {c}, {a}, {b}")
            # Se o b for menor que a
            else:
                # Verifica se o b é menor que o c
                if b < c:
                    # Verifica qual é o segundo e qual é o maior
                    if a < c:
                        print(f"A ordem crescente é: {b}, {a}, {c}")
                    else:
                        print(f"A ordem crescente é: {b}, {c}, {a}")
                # Se o b for maior que c
                else:
                    print(f"A ordem crescente é: {c}, {a}, {b}")