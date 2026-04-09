def addBinary(a: str, b: str) -> str:
    # Преобразуем двоичные строки в целые числа (из двоичной системы в десятичную)
    num1 = int(a, 2)
    num2 = int(b, 2)
    
    # Складываем числа
    sum_num = num1 + num2
    
    # Преобразуем обратно в двоичную строку и убираем префикс '0b'
    return bin(sum_num)[2:]

# Тест
a = "11"
b = "1"
print(addBinary(a, b))  # "100"
