S = input('enter your str:')
S1 = input('enter your symbol:')

S2 = S.replace(S1, S1.upper())

for x in S2:
    if x.upper() in S2:
        ind = S2.rfind(x.upper())
        S2 = (S2[:ind] + S2[ind + 1:])

print(S2)