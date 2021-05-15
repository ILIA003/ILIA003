import os
import time

source = ["C:\\Users\Общие"] # прописываю свой путь

target_dir = 'zip -qr C:\Program . -i Files\GnuWin32\20210515161602.zip' # прописываю свой путь, далее появляется ошибка и я копирую из терминала и вставляю сюда

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today) # mkdir это создание каталога я это в git видел
    print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, '  '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание каталога копии НЕ УДАЛОСЬ')