from get_data import get_data_from_excel
from datetime import datetime, date, timedelta


def num1():
    data = get_data_from_excel('num1')
    return len([x for x in data if int(x) % 2 == 0])


# Мне кажется, такая реализация будет более эффективной с ростом количества входящих данных
def num_1():
    data_int = [int(x) for x in get_data_from_excel('num1')]

    count_even = 0
    res = {}
    for num in data_int:
        try:
            if res[num] == 0:
                count_even += 1
            else:
                continue
        except KeyError:
            if num % 2 == 0:
                count_even += 1
                res[num] = 0
            else:
                res[num] = 1
    return count_even


# так как первые два числа в списке (54, 55) не были простыми, в ручную заменил их на 0, для реализации алгоритма
def num2():
    data_int = [int(x) for x in get_data_from_excel('num2')]
    data_int[0], data_int[1] = 0, 0     # замена 54 и 55 на 0

    n = len(data_int) - 1
    i = 2
    while i <= n:
        if data_int[i] != 0:
            j = i + i
            while j <= n:
                data_int[j] = 0
                j = j + i
        i += 1

    data_int = set(data_int)
    return len(data_int) - 1


def num3():
    data = get_data_from_excel('num3')
    return len([x for x in data if float(x.replace(',', '.').replace(' ', '')) < 0.5])


def date1():
    data = get_data_from_excel('date1')
    return len([x for x in data if x.split()[0] == 'Tue'])


def date2():
    data = get_data_from_excel('date2')
    return len([x for x in data if datetime.strptime(x.split()[0], '%Y-%m-%d').isoweekday() == 2])


def date3():
    data = get_data_from_excel('date3')
    all_tue = [datetime.strptime(x, '%m-%d-%Y') for x in data if datetime.strptime(x, '%m-%d-%Y').isoweekday() == 2]
    return len([x for x in all_tue if (x + timedelta(weeks=1)).month != x.month])

