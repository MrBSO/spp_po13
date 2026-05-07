"""Lab 3, task 2, variant 7.

Структурный паттерн: Bridge.
Автомобили и пульты дистанционного управления
развиваются независимо друг от друга.
"""

from abc import ABC, abstractmethod


class Car(ABC):
    """Абстрактный автомобиль."""

    def __init__(self, model: str) -> None:
        if not model.strip():
            raise ValueError("Модель не может быть пустой.")
        self.model = model
        self.alarm = False
        self.locked = False
        self.engine = False

    @abstractmethod
    def brand(self) -> str:
        """Вернуть марку автомобиля."""

    def activate_alarm(self) -> None:
        """Включить сигнализацию."""
        self.alarm = True
        print(f"{self.brand()} {self.model}: сигнализация включена.")

    def deactivate_alarm(self) -> None:
        """Выключить сигнализацию."""
        self.alarm = False
        print(f"{self.brand()} {self.model}: сигнализация выключена.")

    def lock_doors(self) -> None:
        """Заблокировать двери."""
        self.locked = True
        print(f"{self.brand()} {self.model}: двери заблокированы.")

    def unlock_doors(self) -> None:
        """Разблокировать двери."""
        self.locked = False
        print(f"{self.brand()} {self.model}: двери разблокированы.")

    def start_engine(self) -> None:
        """Запустить двигатель."""
        self.engine = True
        print(f"{self.brand()} {self.model}: двигатель запущен.")

    def stop_engine(self) -> None:
        """Остановить двигатель."""
        self.engine = False
        print(f"{self.brand()} {self.model}: двигатель остановлен.")


# pylint: disable=too-few-public-methods
class BMW(Car):
    """Автомобиль BMW."""

    def brand(self) -> str:
        return "BMW"


# pylint: disable=too-few-public-methods
class Toyota(Car):
    """Автомобиль Toyota."""

    def brand(self) -> str:
        return "Toyota"


# pylint: disable=too-few-public-methods
class Audi(Car):
    """Автомобиль Audi."""

    def brand(self) -> str:
        return "Audi"


# pylint: disable=too-few-public-methods
class RemoteControl(ABC):
    """Абстрактный пульт управления."""

    def __init__(self, car: Car) -> None:
        self.car = car

    @abstractmethod
    def toggle_alarm(self) -> None:
        """Переключить сигнализацию."""

    @abstractmethod
    def toggle_doors(self) -> None:
        """Переключить двери."""

    @abstractmethod
    def toggle_engine(self) -> None:
        """Переключить двигатель."""


class StandardRemote(RemoteControl):
    """Обычный пульт."""

    def toggle_alarm(self) -> None:
        if self.car.alarm:
            self.car.deactivate_alarm()
        else:
            self.car.activate_alarm()

    def toggle_doors(self) -> None:
        if self.car.locked:
            self.car.unlock_doors()
        else:
            self.car.lock_doors()

    def toggle_engine(self) -> None:
        if self.car.engine:
            self.car.stop_engine()
        else:
            self.car.start_engine()


class SecureRemote(RemoteControl):
    """Защищённый пульт."""

    def toggle_alarm(self) -> None:
        print("Проверка безопасности пройдена.")
        if self.car.alarm:
            self.car.deactivate_alarm()
        else:
            self.car.activate_alarm()

    def toggle_doors(self) -> None:
        print("Защищённое управление дверями.")
        if self.car.locked:
            self.car.unlock_doors()
        else:
            self.car.lock_doors()

    def toggle_engine(self) -> None:
        print("Защищённое управление двигателем.")
        if self.car.engine:
            self.car.stop_engine()
        else:
            self.car.start_engine()


def main() -> None:
    """Демонстрация работы паттерна."""
    bmw = BMW("X5")
    toyota = Toyota("Camry")
    audi = Audi("A6")

    standard_remote = StandardRemote(bmw)
    secure_remote = SecureRemote(toyota)
    another_standard_remote = StandardRemote(audi)

    print("=== BMW ===")
    standard_remote.toggle_doors()
    standard_remote.toggle_alarm()
    standard_remote.toggle_engine()

    print("\n=== Toyota ===")
    secure_remote.toggle_doors()
    secure_remote.toggle_alarm()
    secure_remote.toggle_engine()

    print("\n=== Audi ===")
    another_standard_remote.toggle_doors()
    another_standard_remote.toggle_engine()


if __name__ == "__main__":
    main()
