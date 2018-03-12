a = input('how can i call you?(Mr./Mrs./Miss/Ms.):')
if a == 'Mr.' or 'Mrs.':
    print('Dear ', a, 'you male')
elif a == 'Miss' or 'Ms.':
    print('Dear ', a, 'you female')
else:
    print('what are you?')