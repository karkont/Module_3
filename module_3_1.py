# 1.   Функция count_calls подсчитывающая вызовы остальных функций.
# 2.   Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в
#   верхнем регистре, строку в нижнем регистре.
# 3.   Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в
#   этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# 1.   Создать переменную calls = 0 вне функций.
# 2.   Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в
#   остальных двух функциях.
# 3.   Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# 4.   Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# 5.   Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# 6.   Вывести значение переменной calls на экран(в консоль).
calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    le = len(string)
    up = string.upper()
    low = string.lower()
    return le, up, low


def is_contains(string, list_to_search):
    count_calls()
    list_to_search_up = [a.upper() for a in list_to_search]
    if string.upper() in list_to_search_up:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
