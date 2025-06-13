def tem_digito_repetido(num):
    num_str = str(num)
    return len(set(num_str)) != len(num_str)

while True:
    try:
        N, M = map(int, input().split())
        count = 0
        for num in range(N, M + 1):
            if not tem_digito_repetido(num):
                count += 1
        print(count)
    except EOFError:
        break
