from abc import ABC, abstractmethod

# ---------- Реализация (Television) ----------
class Television(ABC):
    @abstractmethod
    def on(self) -> None:
        pass

    @abstractmethod
    def off(self) -> None:
        pass

    @abstractmethod
    def is_on(self) -> bool:
        pass

    @abstractmethod
    def tune_channel(self, channel: int) -> None:
        pass

    @abstractmethod
    def volume_up(self) -> None:
        pass

    @abstractmethod
    def volume_down(self) -> None:
        pass


# Конкретные телевизоры
class SamsungTV(Television):
    def __init__(self):
        self._is_on = False
        self._current_channel = 1
        self._volume = 10

    def on(self) -> None:
        if not self._is_on:
            self._is_on = True
            print("Samsung TV включён")

    def off(self) -> None:
        if self._is_on:
            self._is_on = False
            print("Samsung TV выключен")

    def is_on(self) -> bool:
        return self._is_on

    def tune_channel(self, channel: int) -> None:
        if self._is_on:
            self._current_channel = channel
            print(f"Samsung TV: переключение на канал {channel}")
        else:
            print("Samsung TV выключен, невозможно переключить канал")

    def volume_up(self) -> None:
        if self._is_on:
            self._volume = min(100, self._volume + 5)
            print(f"Samsung TV: громкость +5 -> {self._volume}")

    def volume_down(self) -> None:
        if self._is_on:
            self._volume = max(0, self._volume - 5)
            print(f"Samsung TV: громкость -5 -> {self._volume}")


class LGTV(Television):
    def __init__(self):
        self._is_on = False
        self._current_channel = 1
        self._volume = 10

    def on(self) -> None:
        if not self._is_on:
            self._is_on = True
            print("LG TV включён")

    def off(self) -> None:
        if self._is_on:
            self._is_on = False
            print("LG TV выключен")

    def is_on(self) -> bool:
        return self._is_on

    def tune_channel(self, channel: int) -> None:
        if self._is_on:
            self._current_channel = channel
            print(f"LG TV: установлен канал {channel}")
        else:
            print("LG TV выключен, невозможно установить канал")

    def volume_up(self) -> None:
        if self._is_on:
            self._volume = min(100, self._volume + 2)
            print(f"LG TV: уровень громкости {self._volume}")

    def volume_down(self) -> None:
        if self._is_on:
            self._volume = max(0, self._volume - 2)
            print(f"LG TV: уровень громкости {self._volume}")


# ---------- Абстракция (RemoteControl) ----------
class RemoteControl(ABC):
    def __init__(self, tv: Television):
        self._tv = tv

    @abstractmethod
    def power(self) -> None:
        pass

    @abstractmethod
    def channel_up(self) -> None:
        pass

    @abstractmethod
    def channel_down(self) -> None:
        pass

    @abstractmethod
    def volume_up(self) -> None:
        pass

    @abstractmethod
    def volume_down(self) -> None:
        pass


# Конкретные пульты
class BasicRemote(RemoteControl):
    def power(self) -> None:
        if self._tv.is_on():
            self._tv.off()
        else:
            self._tv.on()

    def channel_up(self) -> None:
        # Упрощённая версия – просто переключает на канал 2 (демонстрация)
        self._tv.tune_channel(2)

    def channel_down(self) -> None:
        self._tv.tune_channel(1)

    def volume_up(self) -> None:
        self._tv.volume_up()

    def volume_down(self) -> None:
        self._tv.volume_down()


class AdvancedRemote(RemoteControl):
    def __init__(self, tv: Television):
        super().__init__(tv)
        self._current_channel = 1

    def power(self) -> None:
        if self._tv.is_on():
            self._tv.off()
        else:
            self._tv.on()

    def channel_up(self) -> None:
        self._current_channel += 1
        self._tv.tune_channel(self._current_channel)

    def channel_down(self) -> None:
        if self._current_channel > 1:
            self._current_channel -= 1
            self._tv.tune_channel(self._current_channel)

    def volume_up(self) -> None:
        self._tv.volume_up()

    def volume_down(self) -> None:
        self._tv.volume_down()

    def mute(self) -> None:
        print("Mute: звук выключен (дополнительная функция AdvancedRemote)")


# ---------- Пример использования ----------
if __name__ == "__main__":
    samsung = SamsungTV()
    lg = LGTV()

    remote_basic = BasicRemote(samsung)
    remote_advanced = AdvancedRemote(lg)

    # Работа с Samsung через BasicRemote
    remote_basic.power()        # Включает Samsung
    remote_basic.volume_up()    # Громкость +5
    remote_basic.channel_up()   # Переключает на канал 2
    remote_basic.power()        # Выключает Samsung

    print("\n--- Работа с LG через AdvancedRemote ---")
    remote_advanced.power()          # Включает LG
    remote_advanced.channel_up()     # Канал 2
    remote_advanced.channel_up()     # Канал 3
    remote_advanced.channel_down()   # Канал 2
    remote_advanced.volume_up()      # Громкость +2
    remote_advanced.volume_up()      # Громкость +2
    remote_advanced.mute()           # Дополнительная функция
    remote_advanced.power()          # Выключает LG
