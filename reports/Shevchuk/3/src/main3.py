"""Lab 3, task 3, variant 7.

Behavioral pattern example: Command.
Pizzeria supports order creation, cancellation and repeating.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Order:
    """Represent an order in the pizzeria."""

    def __init__(self, order_id: int, items: list[str], total_price: float) -> None:
        """Initialize an order."""
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
        self.status = "Created"

    def describe(self) -> str:
        """Return human-readable order description."""
        items_text = ", ".join(self.items)
        left_part = f"Order #{self.order_id}: {items_text}"
        right_part = f"total={self.total_price:.2f} | status={self.status}"
        return f"{left_part} | {right_part}"


class Pizzeria:
    """Represent a pizzeria."""

    PRICE_LIST = {
        "Margherita": 12.0,
        "Pepperoni": 15.0,
        "Four Cheeses": 17.0,
        "Mushroom": 14.0,
        "Cola": 3.0,
        "Juice": 4.0,
    }

    def __init__(self) -> None:
        """Initialize pizzeria storage."""
        self.orders: dict[int, Order] = {}
        self.next_order_id = 1

    def create_order(self, items: list[str]) -> Order:
        """Create a new order."""
        total_price = 0.0

        for item in items:
            if item not in self.PRICE_LIST:
                raise ValueError(f"Menu item '{item}' does not exist.")
            total_price += self.PRICE_LIST[item]

        order = Order(self.next_order_id, items[:], total_price)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1

        print(f"Created {order.describe()}")
        return order

    def cancel_order(self, order_id: int) -> None:
        """Cancel an existing order."""
        order = self.orders.get(order_id)
        if order is None:
            print(f"Order #{order_id} was not found.")
            return

        if order.status == "Cancelled":
            print(f"Order #{order_id} has already been cancelled.")
            return

        order.status = "Cancelled"
        print(f"Order #{order_id} cancelled.")

    def repeat_order(self, order_id: int) -> Order | None:
        """Repeat an existing order."""
        old_order = self.orders.get(order_id)
        if old_order is None:
            print(f"Order #{order_id} was not found.")
            return None

        new_order = self.create_order(old_order.items)
        print(f"Repeated order #{order_id} as order #{new_order.order_id}.")
        return new_order

    def show_orders(self) -> None:
        """Show all orders."""
        print("\nOrders list:")
        if not self.orders:
            print("No orders available.")
            return

        for order in self.orders.values():
            print(order.describe())


class Command(ABC):
    """Abstract command."""

    @abstractmethod
    def execute(self):
        """Execute a command."""


# pylint: disable=too-few-public-methods
class CreateOrderCommand(Command):
    """Command for order creation."""

    def __init__(self, pizzeria: Pizzeria, items: list[str]) -> None:
        """Initialize the command."""
        self.pizzeria = pizzeria
        self.items = items

    def execute(self) -> Order:
        """Execute the command."""
        return self.pizzeria.create_order(self.items)


# pylint: disable=too-few-public-methods
class CancelOrderCommand(Command):
    """Command for order cancellation."""

    def __init__(self, pizzeria: Pizzeria, order_id: int) -> None:
        """Initialize the command."""
        self.pizzeria = pizzeria
        self.order_id = order_id

    def execute(self) -> None:
        """Execute the command."""
        self.pizzeria.cancel_order(self.order_id)


# pylint: disable=too-few-public-methods
class RepeatOrderCommand(Command):
    """Command for order repeating."""

    def __init__(self, pizzeria: Pizzeria, order_id: int) -> None:
        """Initialize the command."""
        self.pizzeria = pizzeria
        self.order_id = order_id

    def execute(self) -> Order | None:
        """Execute the command."""
        return self.pizzeria.repeat_order(self.order_id)


class OrderManager:
    """Manage command execution."""

    def __init__(self) -> None:
        """Initialize command manager."""
        self.history: list[str] = []

    def run_command(self, command: Command):
        """Execute a command and remember it."""
        result = command.execute()
        self.history.append(command.__class__.__name__)
        return result

    def show_history(self) -> None:
        """Show command execution history."""
        print("\nCommand history:")
        if not self.history:
            print("History is empty.")
            return

        for index, command_name in enumerate(self.history, start=1):
            print(f"{index}. {command_name}")


def main() -> None:
    """Demonstrate the command example."""
    pizzeria = Pizzeria()
    manager = OrderManager()

    create_first_order = CreateOrderCommand(pizzeria, ["Pepperoni", "Cola"])
    first_order = manager.run_command(create_first_order)

    create_second_order = CreateOrderCommand(pizzeria, ["Margherita", "Juice"])
    second_order = manager.run_command(create_second_order)

    cancel_first_order = CancelOrderCommand(pizzeria, first_order.order_id)
    manager.run_command(cancel_first_order)

    repeat_second_order = RepeatOrderCommand(pizzeria, second_order.order_id)
    manager.run_command(repeat_second_order)

    pizzeria.show_orders()
    manager.show_history()


if __name__ == "__main__":
    main()
