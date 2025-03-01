def product_of_numbers(num1, num2):
    return num1 * num2

def factorial(num):
    a = 1
    for i in range(1, num+1):
        a = a * i
    return a

def min_number(data):
    return min(data)


print(product_of_numbers(2,5)) #1

print(factorial(5)) #2

print(min_number([1,2,3])) #4