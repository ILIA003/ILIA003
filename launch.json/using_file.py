poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
        используй Python!'''

f = open('poem.txt', 'w') # открываю файл для записи
f.write(poem) # записываю файл
f.close() # закрываю файл

while True:
    line = f.readline( )
    if len(line) == 1:
        break
    print(line, end=' ')

f.close()