l = []
count = 0

while True:
    n = input('enter your numbers: ')
    if n.isnumeric():
        l.append(int(n))
    if n == '' or n == ' ':
        break
    else:
        continue

no = int(input('enter number: '))

for x in l:
    if x == no:
        count += 1

print('your number is there {}'.format(count), 'times')