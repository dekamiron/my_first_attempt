search = input('введите ключевое слово для поиска(фамилия, имя, пол, возраст): ')

Base = [[('s_name', 'Petrov'), ('name', 'Petya'), ('sex', 'male'), ('age', '22')],
        [('s_name', 'Ivanov'), ('name', 'Vanya'), ('sex', 'male'), ('age', '25')],
        [('s_name', 'Petrov'), ('name', 'Vasya'), ('sex', 'male'), ('age', '44')]
        ]

for i in Base:
    for j in i:
        if search in j:
            print(Base.index(i)+1, 'Фамилия: %s Имя: %s Пол: %s возраст %s' \
                  % (i[0][1], i[1][1], i[2][1], i[3][1]))
        else:
            print('В базе нет таких людей')