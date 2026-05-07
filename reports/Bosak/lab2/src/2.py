class Abiturient:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def avg_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def is_admitted(self):
        return self.avg_grade() >= 60

class Faculty:
    def __init__(self, name):
        self.name = name
        self.abiturients = []
    
    def register(self, abiturient):
        self.abiturients.append(abiturient)

print("=== Система вступительных экзаменов ===")
faculty = Faculty(input("Название факультета: "))

num = int(input("Сколько абитуриентов? "))

for i in range(num):
    name = input(f"\nИмя абитуриента {i+1}: ")
    ab = Abiturient(name)
    faculty.register(ab)
    
    exam_count = int(input(f"Сколько экзаменов сдает {name}? "))
    for j in range(exam_count):
        exam_name = input(f"  Название экзамена {j+1}: ")
        teacher = input(f"  Преподаватель: ")
        grade = float(input(f"  Оценка: "))
        ab.add_grade(grade)

print("\n=== Результаты ===")
for ab in faculty.abiturients:
    print(f"{ab.name}: средний балл = {ab.avg_grade():.2f}, зачислен: {ab.is_admitted()}")