def eh_perfeito(x):
    if x == 1:
        return False  
    soma = 1  
    i = 2
    while i * i <= x:
        if x % i == 0:
            soma += i
            outro = x // i
            if outro != i:
                soma += outro
        i += 1
    return soma == x

N = int(input())
for _ in range(N):
    X = int(input())
    if eh_perfeito(X):
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
