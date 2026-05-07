from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

class ChocolateBar(Product):
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self) -> str:
        return f"Шоколадный батончик '{self._name}'"

    def get_price(self) -> float:
        return self._price

class Chips(Product):
    def __init__(self, flavor: str, price: float):
        self._flavor = flavor
        self._price = price

    def get_name(self) -> str:
        return f"Чипсы со вкусом '{self._flavor}'"

    def get_price(self) -> float:
        return self._price

class Juice(Product):
    def __init__(self, fruit: str, volume_ml: int, price: float):
        self._fruit = fruit
        self._volume = volume_ml
        self._price = price

    def get_name(self) -> str:
        return f"Сок '{self._fruit}' {self._volume} мл"

    def get_price(self) -> float:
        return self._price

class VendingMachine(ABC):
    @abstractmethod
    def create_product(self, product_type: str, **kwargs) -> Product:
        """Фабричный метод для создания товара"""

    def dispense_product(self, product_type: str, **kwargs) -> None:
        """Метод для выдачи товара"""
        product = self.create_product(product_type, **kwargs)
        print(f"Автомат выдаёт: {product.get_name()} за {product.get_price()} руб.")

class SnackVendingMachine(VendingMachine):
    def create_product(self, product_type: str, **kwargs) -> Product:
        if product_type == "chocolate":
            return ChocolateBar(kwargs.get("name", "Unknown"), kwargs.get("price", 0.0))
        if product_type == "chips":
            return Chips(kwargs.get("flavor", "Unknown"), kwargs.get("price", 0.0))
        if product_type == "juice":
            return Juice(kwargs.get("fruit", "Unknown"), kwargs.get("volume", 0), kwargs.get("price", 0.0))
        raise ValueError(f"Неизвестный тип товара: {product_type}")

if __name__ == "__main__":
    machine = SnackVendingMachine()
    machine.dispense_product("chocolate", name="Mars", price=75.0)
    machine.dispense_product("chips", flavor="Сметана и лук", price=60.0)
    machine.dispense_product("juice", fruit="Апельсин", volume=330, price=100.0)
