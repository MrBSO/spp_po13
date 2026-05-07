class Tour:
    def __init__(self):
        self.transport = None
        self.hotel = None
        self.food = None
        self.excursions = []
        self.price = 0
    
    def __str__(self):
        return f"Тур: {self.transport}, {self.hotel}, питание: {self.food}, экскурсии: {self.excursions}, цена: {self.price}"

class TourBuilder:
    def __init__(self):
        self.tour = Tour()
    
    def add_transport(self, transport, cost):
        self.tour.transport = transport
        self.tour.price += cost
        return self
    
    def add_hotel(self, hotel, cost):
        self.tour.hotel = hotel
        self.tour.price += cost
        return self
    
    def add_food(self, food, cost):
        self.tour.food = food
        self.tour.price += cost
        return self
    
    def add_excursion(self, excursion, cost):
        self.tour.excursions.append(excursion)
        self.tour.price += cost
        return self
    
    def build(self):
        return self.tour

print("=== Туристическое бюро ===")
builder = TourBuilder()

print("\nВыберите транспорт:")
print("1 - Самолет (300$)")
print("2 - Поезд (150$)")
print("3 - Автобус (100$)")
choice = input("Ваш выбор: ")
if choice == "1":
    builder.add_transport("Самолет", 300)
elif choice == "2":
    builder.add_transport("Поезд", 150)
else:
    builder.add_transport("Автобус", 100)

print("\nВыберите проживание:")
print("1 - Отель 5* (500$)")
print("2 - Отель 3* (300$)")
print("3 - Хостел (100$)")
choice = input("Ваш выбор: ")
if choice == "1":
    builder.add_hotel("Отель 5*", 500)
elif choice == "2":
    builder.add_hotel("Отель 3*", 300)
else:
    builder.add_hotel("Хостел", 100)

print("\nВыберите питание:")
print("1 - Все включено (200$)")
print("2 - Завтрак+ужин (100$)")
print("3 - Без питания (0$)")
choice = input("Ваш выбор: ")
if choice == "1":
    builder.add_food("Все включено", 200)
elif choice == "2":
    builder.add_food("Завтрак+ужин", 100)
else:
    builder.add_food("Без питания", 0)

print("\nДобавьте экскурсии (введите 'stop' для завершения):")
while True:
    print("1 - Обзорная экскурсия (50$)")
    print("2 - Музей (30$)")
    print("3 - Выставка (40$)")
    print("stop - закончить")
    choice = input("Ваш выбор: ")
    if choice == "1":
        builder.add_excursion("Обзорная экскурсия", 50)
    elif choice == "2":
        builder.add_excursion("Музей", 30)
    elif choice == "3":
        builder.add_excursion("Выставка", 40)
    elif choice == "stop":
        break

tour = builder.build()
print("\n=== Ваш тур ===")
print(tour)