history = []
score = 0

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
        history.append(f'{name}: {buy}')
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
        print('История покупок:', history)
    elif choice == '4':
        print('Программа завершена.')
        break
    else:
        print('Неверный номер действия. Повторите ввод.')