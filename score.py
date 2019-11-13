import os
import json


FILE_NAME = 'score.json'
FILE_HISTORY = 'history.txt'


history = []
if os.path.exists(FILE_HISTORY):
    with open(FILE_HISTORY, 'r') as f:
        for order in f:
            history.append(order.replace('\n', ''))

score = 0
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        score = json.load(f)

#else:
#    orders = {'score': 0, 'history': []}


def replenishment(score):
    sum = int(input('Введите сумму для пополнения счёта:'))
    score += sum
    print('У Вас на счету:', score)
    return score

def purchase(score):
    buy = int(input('Введите стоимость покупки:'))
    if buy <= score:
        score -= buy
        name = input('Введите название товара:')
        print('Успешно. У Вас на счету:', score)
        order = (name, buy)
        history.append(order)
        return score
    else:
        print('У Вас на счету недостаточно средств.')
    return score

while True:
    print('У вас на счету:', score)
    print('1. Пополнение счета')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Выход')

    choice = input('Введите номер действия:')
    if choice == '1':
        score = replenishment(score)
    elif choice == '2':
        score = purchase(score)
    elif choice == '3':
        for order in history:
            print(order)
    elif choice == '4':
        with open('score.json', 'w') as f:
            json.dump(score, f)
        with open(FILE_HISTORY, 'w') as f:
            for order in history:
                f.write(f'{order}\n')
        print('Программа завершена.')
        break
    else:
        print('Неверный номер действия. Повторите ввод.')