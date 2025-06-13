n = int(input())

epr = 0
ehd = 0
intrusos = 0

for _ in range(n):
    linha = input().split()
    matricula, curso = linha[0], linha[1]

    if curso == "EPR":
        epr += 1
    elif curso == "EHD":
        ehd += 1
    else:
        intrusos += 1

print(f"EPR: {epr}")
print(f"EHD: {ehd}")
print(f"INTRUSOS: {intrusos}")
