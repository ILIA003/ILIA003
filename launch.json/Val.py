try:
    f = open('simple.txt', 'w')
    f.write('Test write to simple text!')
except IOError:
    print('Не удалось записать текст')
else:
    print('Удалось записать текст')
    f.close()