def sum_of_numbers(a, b):
    return a + b


def max_number(data):
    return max(data)


def number_is_palindrom(num):
    num = str(num)
    return num[:] == num[::-1]


def average_number(data):
    return sum(data) / len(data)


def sum_of_list(data):
    a = 0
    for i in range(len(data)):
        a += data[i]
    return a


def max_in_list(data):
    a = data[0]
    for i in range(len(data)):
        if a < data[i]:
            a = data[i]
    return a


def count_iven_numbers(data):
    a = 0
    for i in range(len(data)):
        if data[i] % 2 == 0:
            a += 1
    return a


def count_simbols(stroke, simbol):
    a = 0
    for i in range(len(stroke)):
        if simbol == stroke[i]:
            a += 1
    return a


print(count_simbols('hello', 'l'))