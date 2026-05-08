from abc import ABC, abstractmethod
from typing import List, Optional
import os

# ---------- Модель файла (получатель) ----------
class TextFile:
    def __init__(self, path: str):
        self.path = path
        self._content: Optional[str] = None

    def read(self) -> str:
        with open(self.path, 'r', encoding='utf-8') as file_handle:
            self._content = file_handle.read()
        return self._content

    def write(self, new_content: str) -> None:
        with open(self.path, 'w', encoding='utf-8') as file_handle:
            file_handle.write(new_content)
        self._content = new_content

    def get_content(self) -> Optional[str]:
        return self._content

# ---------- Базовый класс команды ----------
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

# ---------- Конкретные команды ----------
class ReadFileCommand(Command):
    def __init__(self, file: TextFile):
        self._file = file
        self._result: Optional[str] = None

    def execute(self) -> None:
        self._result = self._file.read()
        print(f"Прочитан файл {self._file.path}: {self._result[:50]}...")

    def undo(self) -> None:
        print(f"Отмена чтения файла {self._file.path} не нужна")

class ModifyFileCommand(Command):
    def __init__(self, file: TextFile, new_content: str):
        self._file = file
        self._new_content = new_content
        self._old_content: Optional[str] = None

    def execute(self) -> None:
        self._old_content = self._file.get_content()
        if self._old_content is None:
            self._old_content = self._file.read()
        self._file.write(self._new_content)
        print(f"Файл {self._file.path} изменён")

    def undo(self) -> None:
        if self._old_content is not None:
            self._file.write(self._old_content)
            print(f"Изменение файла {self._file.path} отменено (восстановлено предыдущее содержимое)")
        else:
            print("Нечего отменять")

# Макрокоманда для последовательного выполнения нескольких операций
class MacroCommand(Command):
    def __init__(self, commands: List[Command]):
        self._commands = commands

    def execute(self) -> None:
        print("Выполнение сложной операции (последовательность команд):")
        for cmd in self._commands:
            cmd.execute()

    def undo(self) -> None:
        print("Отмена сложной операции (отмена всех подкоманд в обратном порядке):")
        for cmd in reversed(self._commands):
            cmd.undo()

# ---------- Управляющий класс (Invoker) с историей команд ----------
class FileCommandProcessor:
    def __init__(self):
        self._history: List[Command] = []

    def execute_command(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo_last(self) -> None:
        if self._history:
            cmd = self._history.pop()
            cmd.undo()
        else:
            print("Нет операций для отмены")

    def undo_all(self) -> None:
        while self._history:
            self.undo_last()

# ---------- Пример использования ----------
if __name__ == "__main__":
    # Создадим тестовые файлы
    with open("test1.txt", "w", encoding="utf-8") as file1_handle:
        file1_handle.write("Привет, мир!")
    with open("test2.txt", "w", encoding="utf-8") as file2_handle:
        file2_handle.write("Старое содержимое")

    file1 = TextFile("test1.txt")
    file2 = TextFile("test2.txt")

    processor = FileCommandProcessor()

    read_cmd = ReadFileCommand(file1)
    modify_cmd1 = ModifyFileCommand(file2, "Новое содержимое файла 2")

    processor.execute_command(read_cmd)
    processor.execute_command(modify_cmd1)

    print("\n--- Проверка содержимого file2 после изменения ---")
    print(file2.read())

    processor.undo_last()
    print("\n--- После отмены изменения file2 ---")
    print(file2.read())

    modify_cmd2 = ModifyFileCommand(file1, "Мир, привет!")
    modify_cmd3 = ModifyFileCommand(file2, "Ещё одна правка")
    macro = MacroCommand([modify_cmd2, modify_cmd3])

    processor.execute_command(macro)
    print("\n--- После выполнения сложной операции ---")
    print(f"file1: {file1.read()}")
    print(f"file2: {file2.read()}")

    processor.undo_last()
    print("\n--- После отмены сложной операции ---")
    print(f"file1: {file1.read()}")
    print(f"file2: {file2.read()}")

    os.remove("test1.txt")
    os.remove("test2.txt")
