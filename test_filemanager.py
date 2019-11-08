import os
from functions_for_filemaneger import add_dir, del_dir, copy_dir

def test_add_dir():
    os.mkdir(test_dir)
    assert 'test_dir' in os.listdir()
    os.rmdir(test_dir)

def test_choice(choice):
    return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)


def test_random():
    import victorin
    x = set([victorin])
    return(x)

def test_cross():
    y = len((lambda x: os.path.isdir(y), os.listdir()) & (lambda x: os.path.isfile(y), os.listdir()))
    if x > 0:
        return Fulse
    else:
        print('Error')

