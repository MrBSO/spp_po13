"""Module implementing IntegerSet class for working with sets of integers."""

from typing import List, Optional


class IntegerSet:
    """A class representing a set of integers."""

    def __init__(self, initial_elements: Optional[List[int]] = None) -> None:
        """
        Initialize IntegerSet with optional initial elements.

        Args:
            initial_elements: List of integers to initialize the set with.
        """
        if initial_elements is None:
            self.elements: List[int] = []
        else:
            self.elements = []
            seen = set()
            for x in initial_elements:
                if x not in seen:
                    seen.add(x)
                    self.elements.append(x)

    def add(self, element: int) -> None:
        """Add an element to the set if not already present."""
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element: int) -> None:
        """Remove an element from the set if present."""
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element: int) -> bool:
        """Check if element exists in the set."""
        return element in self.elements

    def intersection(self, other: 'IntegerSet') -> 'IntegerSet':
        """Return a new IntegerSet with elements common to both sets."""
        result = IntegerSet()
        for x in self.elements:
            if x in other.elements:
                result.add(x)
        return result

    def __str__(self) -> str:
        """Return string representation of the set."""
        if not self.elements:
            return "{}"
        return "{" + ", ".join(str(x) for x in sorted(self.elements)) + "}"

    def __eq__(self, other: object) -> bool:
        """Check equality between two IntegerSet objects."""
        if not isinstance(other, IntegerSet):
            return False
        return sorted(self.elements) == sorted(other.elements)


def main() -> None:
    """Main function to demonstrate IntegerSet usage."""
    print("=== Работа с множеством целых чисел ===")

    input1 = input("Введите элементы первого множества через пробел: ")
    nums1 = [int(x) for x in input1.split()]
    set1 = IntegerSet(nums1)

    input2 = input("Введите элементы второго множества через пробел: ")
    nums2 = [int(x) for x in input2.split()]
    set2 = IntegerSet(nums2)

    print(f"Первое множество: {set1}")
    print(f"Второе множество: {set2}")
    print(f"Пересечение: {set1.intersection(set2)}")

    val = int(input("Введите число для проверки в первом множестве: "))
    print(f"Число {val} принадлежит первому множеству? {set1.contains(val)}")

    add_val = int(input("Введите число для добавления в первое множество: "))
    set1.add(add_val)
    print(f"После добавления: {set1}")

    rem_val = int(input("Введите число для удаления из первого множества: "))
    set1.remove(rem_val)
    print(f"После удаления: {set1}")

    print(f"Множества равны? {set1 == set2}")


if __name__ == "__main__":
    main()
