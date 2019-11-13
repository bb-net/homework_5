import os
import sys
import json

listdir = {
        'files': [],
        'dirs': [],
}
def list_dir():
    for file in os.listdir():
        if os.path.isfile(file):
            listdir['files'].append(file)
        else:
            listdir['dirs'].append(file)
    with open('listdir.txt', 'w') as f:
        json.dump(listdir, f)
    print('Успешно сохранено "listdir.txt" в:', os.getcwd())


while True:
    print("""
    1. Создать папку
    2. Удалить (файл/папку)
    3. Копировать (файл/папку)
    4. Просмотр содержимого рабочей директории
    5. Посмотреть только папки
    6. Посмотреть только файлы
    7. Просмотр информации об операционной системе
    8. Создатель программы
    9. Играть в викторину
    10. Счет
    11. Смена рабочей директории
    12. Сохранить содержимое рабочей директории в файл
    13. Выход
    """)

    choice = input('Введите номер действия:')
    if choice == '1': # Создание папки
        from functions_for_filemaneger import add_dir
        for i in range(1):
            add_dir()
    elif choice == '2': # Удаление папки или файла
        from functions_for_filemaneger import del_dir
        for i in range(1):
            del_dir()
    elif choice == '3': # Копирование папки или файла
        from functions_for_filemaneger import copy_dir
        for i in range(1):
            copy_dir()
    elif choice == '4': # Просмотр содержимого рабочей директории
        print('\n'.join(os.listdir()))
    elif choice == '5': # Посмотреть только папки
        print('\n'.join(filter(lambda x: os.path.isdir(x), os.listdir())))
    elif choice == '6':  # Посмотреть только файлы
        print('\n'.join(filter(lambda x: os.path.isfile(x), os.listdir())))
    elif choice == '7': # Информация о системе
        print(os.name)
    elif choice == '8': # Создатель программы
        print('© 2019 BB')
    elif choice == '9': # Викторина
        import victorin
    elif choice == '10':  # Счет
        import score
    elif choice == '11':  # Смена рабочей директории
        from functions_for_filemaneger import ch_dir
        for i in range(1):
            ch_dir()
    elif choice == '12': # Сохранение раб директории в файл
        list_dir()
    elif choice == '13': # Выход
        print('Программа завершена.')
        break
    else:
        print('Неверный номер действия. Повторите ввод.')