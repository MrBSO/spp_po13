"""Lab 3, task 3, variant 7.

Поведенческий паттерн: Command.
Пиццерия поддерживает создание заказа,
его отмену и повтор.
"""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Order:
    """Сущность заказа."""

    def __init__(self, order_id: int, items: list[str]) -> None:
        self.order_id = order_id
        self.items = items
        self.status = "Создан"

    def info(self) -> str:
        """Вернуть описание заказа."""
        items_text = ", ".join(self.items)
        return f"Заказ №{self.order_id}: {items_text}, статус={self.status}"


class Pizzeria:
    """Получатель команд."""

    def __init__(self) -> None:
        self.orders: dict[int, Order] = {}
        self.next_id = 1

    def create_order(self, items: list[str]) -> Order:
        """Создать заказ."""
        order = Order(self.next_id, items)
        self.orders[self.next_id] = order
        self.next_id += 1
        print(f"Создан {order.info()}")
        return order

    def cancel_order(self, order_id: int) -> None:
        """Отменить заказ."""
        order = self.orders.get(order_id)
        if order is None:
            print(f"Заказ №{order_id} не найден.")
            return

        order.status = "Отменён"
        print(f"Заказ №{order_id} отменён.")

    def repeat_order(self, order_id: int) -> Order | None:
        """Повторить заказ."""
        old_order = self.orders.get(order_id)
        if old_order is None:
            print(f"Заказ №{order_id} не найден.")
            return None

        return self.create_order(old_order.items)


# pylint: disable=too-few-public-methods
class Command(ABC):
    """Абстрактная команда."""

    @abstractmethod
    def execute(self):
        """Выполнить команду."""


# pylint: disable=too-few-public-methods
class CreateOrderCommand(Command):
    """Команда создания заказа."""

    def __init__(self, pizzeria: Pizzeria, items: list[str]) -> None:
        self.pizzeria = pizzeria
        self.items = items

    def execute(self) -> Order:
        return self.pizzeria.create_order(self.items)


# pylint: disable=too-few-public-methods
class CancelOrderCommand(Command):
    """Команда отмены заказа."""

    def __init__(self, pizzeria: Pizzeria, order_id: int) -> None:
        self.pizzeria = pizzeria
        self.order_id = order_id

    def execute(self) -> None:
        self.pizzeria.cancel_order(self.order_id)


# pylint: disable=too-few-public-methods
class RepeatOrderCommand(Command):
    """Команда повтора заказа."""

    def __init__(self, pizzeria: Pizzeria, order_id: int) -> None:
        self.pizzeria = pizzeria
        self.order_id = order_id

    def execute(self) -> Order | None:
        return self.pizzeria.repeat_order(self.order_id)


class OrderManager:
    """Вызывающий объект."""

    def __init__(self) -> None:
        self.history: list[str] = []

    def run(self, command: Command):
        """Запустить команду и сохранить её в историю."""
        result = command.execute()
        self.history.append(command.__class__.__name__)
        return result


def main() -> None:
    """Демонстрация работы паттерна."""
    pizzeria = Pizzeria()
    manager = OrderManager()

    first_order = manager.run(CreateOrderCommand(pizzeria, ["Пепперони", "Кола"]))
    second_order = manager.run(CreateOrderCommand(pizzeria, ["Маргарита", "Сок"]))

    manager.run(CancelOrderCommand(pizzeria, first_order.order_id))
    manager.run(RepeatOrderCommand(pizzeria, second_order.order_id))

    print("\nИстория команд:")
    for item in manager.history:
        print(item)


if __name__ == "__main__":
    main()
