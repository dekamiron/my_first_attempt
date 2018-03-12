N = input('enter your numbers:')
N1 = list(map(int, N.split()))

for x in N1:
    if x == 0:
        N1.remove(x)
        N1.append(1)

print(N1)