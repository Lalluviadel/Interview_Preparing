"""
Написать программу «Банковский депозит».
Клиент банка делает депозит на определенный срок.

В зависимости от суммы и срока вклада определяется процентная ставка:
- 1000–10000 руб.
    (6 месяцев — 5 % годовых,
    год — 6 % годовых,
    2 и более года — 5 % годовых).

-10000–100000 руб.
    (6 месяцев — 6 % годовых,
    год — 7 % годовых,
    2 и более года – 6.5 % годовых).

- 100000–1000000 руб.
    (6 месяцев — 7 % годовых,
    год — 8 % годовых,
    2 и более года — 7.5 % годовых).

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму вклада
на конец срока.
"""


def calc_deposit_amount(data_dict, amount, period):
    try:
        if 6 <= period < 12:
            percent = data_dict['6']
        elif 12 <= period < 24:
            percent = data_dict['12']
        elif period >= 24:
            percent = data_dict['24']
        else:
            print('Вы ввели неверный период в месяцах')
            return
        for i in range(period):
            current_accruals = amount / 100 * percent / 12
            amount += current_accruals
        return round(amount, 2), percent
    except TypeError:
        print('Период должен быть числом')


def bank_deposit(deposit_amount, period):
    tiny_deposit = {'6': 5, '12': 6, '24': 5}
    medium_deposit = {'6': 6, '12': 7, '24': 6.5}
    large_deposit = {'6': 7, '12': 8, '24': 7.5}

    try:
        if 1000 <= deposit_amount < 10000:
            result, percent = calc_deposit_amount(tiny_deposit, deposit_amount, period)
        elif 10000 <= deposit_amount < 100000:
            result, percent = calc_deposit_amount(medium_deposit, deposit_amount, period)
        elif 100000 <= deposit_amount < 1000000:
            result, percent = calc_deposit_amount(large_deposit, deposit_amount, period)
        else:
            print('Вы ввели неверную сумму')
            return
        if result:
            print(f'Начальная сумма: {deposit_amount}\n'
                  f'Процентная ставка: {percent}\n'
                  f'Срок: {period}\n'
                  f'Сумма вклада на конец срока: {result}')
    except TypeError:
        print('Сумма должна быть числом')


bank_deposit(500000, 6)
