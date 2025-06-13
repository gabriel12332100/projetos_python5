N = int(input())

for _ in range(N):
    joao_pontos = 0
    for _ in range(3):
        X, D = map(int, input().split())
        joao_pontos += X * D

    maria_pontos = 0
    for _ in range(3):
        X, D = map(int, input().split())
        maria_pontos += X * D

    if joao_pontos > maria_pontos:
        print("JOAO")
    else:
        print("MARIA")
