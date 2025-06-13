def eh_primo(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

N = int(input())
for _ in range(N):
    X = int(input())
    if eh_primo(X):
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")
