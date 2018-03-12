s = 'Hello!Antony!Have!A!Good!Day!'
s = list(s.split('!'))
s = [x.upper() for x in s if x != '']
print(s)