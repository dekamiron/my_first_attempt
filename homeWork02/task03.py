st = []
c = 1

while True:
    print(c, end='-я: ')
    c += 1
    n = input()
    if not n == '':
        st.append(str(n))
    else:
        break

ind = 0
for x in range(1, len(st)):
    if len(st[x]) > len(st[ind]):
        ind = x

for x in range(len(st)):
    if len(st[x]) == len(st[ind]):
        print(x + 1, 'строка')