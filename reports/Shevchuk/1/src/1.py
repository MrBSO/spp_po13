# pylint: disable=invalid-name

"""Лабораторная работа 1, задание 1, вариант 7.

Программа принимает последовательность целых чисел и выводит её медиану.
"""

from typing import List, Union


def parse_numbers(text: str) -> List[int]:
    """Преобразует строку с целыми числами в список int."""
    parts = text.split()
    if not parts:
        raise ValueError("Пустой ввод")

    numbers = [int(item) for item in parts]
    return numbers


def calculate_median(numbers: List[int]) -> Union[int, float]:
    """Возвращает медиану последовательности."""
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle = length // 2

    if length % 2 == 1:
        return sorted_numbers[middle]

    return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2


def main() -> None:
    """Точка входа в программу."""
    raw_input_data = input("Введите последовательность целых чисел через пробел: ")

    try:
        numbers = parse_numbers(raw_input_data)
    except ValueError:
        print("Ошибка: введите непустую последовательность целых чисел.")
        return

    median = calculate_median(numbers)
    print(f"Медиана последовательности: {median}")


if __name__ == "__main__":
    main()
