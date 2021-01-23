def get_digit(number, n):
    return number // 10**n % 10


a = int(input())
b = get_digit(a, 1)
print(b)
