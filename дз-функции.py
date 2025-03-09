def product_of_numbers(num1, num2):
    return num1 * num2


def factorial(num):
    a = 1
    for i in range(1, num + 1):
        a = a * i
    return a


def min_number(data):
    a = data[0]
    for i in range(len(data)):
        if a > data[i]:
            a = data[i]
    return a


print(product_of_numbers(2, 5))  # 1

print(factorial(5))  # 2

print(min_number([1, 2, 3]))  # 4
