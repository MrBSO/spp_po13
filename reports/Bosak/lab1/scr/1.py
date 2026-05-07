def sum_squares_negative(numbers):
    return sum(x**2 for x in numbers if x < 0)

numbers = list(map(int, input().split()))
result = sum_squares_negative(numbers)
print(result)