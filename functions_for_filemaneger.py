import os
import shutil
import sys

def add_dir():

    new_catalog = input('Введите имя файла:')
    try:
        os.mkdir(new_catalog)
    except OSError:
        print('Директорию %s не удалось создать!' % new_catalog)
    else:
        print('Директория %s успешно создана.' % new_catalog)

def del_dir():

    del_catalog = input('Введите имя файла или папки:')
    try:
        os.rmdir(del_catalog)
    except OSError:
        print('Удалить %s не удалось!' % del_catalog)
    else:
        print('%s успешно удалено.' % del_catalog)

def copy_dir():
    origin_catalog = input('Введите имя файла или папки для копирования:')
    clone_catalog = input('Введите новое имя файла или папки:')
    if os.path.isdir(origin_catalog):
        try:
            shutil.copytree(origin_catalog,  clone_catalog)
        except OSError:
            print('Копирование не удалось!')
        else:
            print('%s успешно скопирован.' % clone_catalog)
    else:
        try:
            shutil.copy(origin_catalog,  clone_catalog)
        except OSError:
            print('Копирование не удалось!')
        else:
            print('%s успешно скопирован.' % clone_catalog)

def ch_dir():
    ch_catalog = tuple(os.listdir())
    try:
        ch_dir = os.chdir(ch_catalog)
    except OSError:
        print('Запрос не выполнен')
    else:
        print('Новая директория:', ch_catalog)

def look_dir():
    if os.path.isdir(ch_catalog):
        print()
    #if os.path.isdir(look_catalog):
    #    try:
    #        shutil.copytree(origin_catalog,  clone_catalog)
    #    except OSError:
    #        print('Копирование не удалось!')
    #    else:
    #        print('%s успешно скопирован.' % clone_catalog)
    #else:
    #    try:
    #        shutil.copy(origin_catalog,  clone_catalog)
    #    except OSError:
    #        print('Копирование не удалось!')
    #    else:
    #        print('%s успешно скопирован.' % clone_catalog)