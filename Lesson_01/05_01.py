"""
Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная
сумма пополнения вклада.
Считаем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего.
Если 3-м аргументом передан 0, то вызов должен быть совпадать с задачей 4.
"""


def calc_deposit_amount(data_dict, amount, period, replenishment):
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
            if 0 < i < period-1:
                amount += replenishment
        return round(amount, 2), percent
    except TypeError:
        print('Период должен быть числом')


def bank_deposit(deposit_amount, period, replenishment=0):
    tiny_deposit = {'6': 5, '12': 6, '24': 5}
    medium_deposit = {'6': 6, '12': 7, '24': 6.5}
    large_deposit = {'6': 7, '12': 8, '24': 7.5}

    try:
        if 1000 <= deposit_amount < 10000:
            result, percent = calc_deposit_amount(tiny_deposit, deposit_amount, period, replenishment)
        elif 10000 <= deposit_amount < 100000:
            result, percent = calc_deposit_amount(medium_deposit, deposit_amount, period, replenishment)
        elif 100000 <= deposit_amount < 1000000:
            result, percent = calc_deposit_amount(large_deposit, deposit_amount, period, replenishment)
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


bank_deposit(500000, 6, 15000)
bank_deposit(500000, 6)
