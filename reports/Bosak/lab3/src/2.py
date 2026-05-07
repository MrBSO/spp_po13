from datetime import datetime

class File:
    def __init__(self, name, size, ext):
        self.name = name
        self.size = size
        self.ext = ext
        self.created = datetime.now()
    
    def __str__(self):
        return f"Файл: {self.name}.{self.ext}, размер: {self.size}KB, создан: {self.created.date()}"

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def get_size(self):
        return sum(c.size if isinstance(c, File) else c.get_size() for c in self.children)
    
    def __str__(self):
        return f"Папка: {self.name}, размер: {self.get_size()}KB"

def show_structure(item, level=0):
    indent = "  " * level
    print(indent + str(item))
    if isinstance(item, Directory):
        for child in item.children:
            show_structure(child, level + 1)

print("=== Файловая система ===")
root = Directory(input("Имя корневой папки: "))

while True:
    print("\n1 - Добавить папку")
    print("2 - Добавить файл")
    print("3 - Показать структуру")
    print("4 - Выход")
    choice = input("Выбор: ")
    
    if choice == "1":
        name = input("Имя папки: ")
        root.add(Directory(name))
        print(f"Папка '{name}' добавлена")
    
    elif choice == "2":
        name = input("Имя файла: ")
        size = int(input("Размер (KB): "))
        ext = input("Расширение: ")
        root.add(File(name, size, ext))
        print(f"Файл '{name}.{ext}' добавлен")
    
    elif choice == "3":
        print("\n=== Структура ФС ===")
        show_structure(root)
    
    elif choice == "4":
        break