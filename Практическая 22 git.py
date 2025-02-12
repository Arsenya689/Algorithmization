class Hotel:
    """Placeholder documentation"""
    def __init__(self, name):
        self.name = name
    
    rooms = {101:True, 102:True, 103:True, 104:True,
             201:True, 202:True, 203:True, 204:True}
    
    def info(self):
        print(f"\nОтель: {self.name}")
        for room in self.rooms:
            if self.rooms[room] == True:
                print(f"Комната {room} свободна")
            else:
                print(f"Комната {room} занята")
    
    def book(self, room):
        if room in self.rooms:
            if self.rooms[room]:
                self.rooms[room] = False
                print(f"\nКомната {room} забронирована")
            else:
                print(f"\nНомер {room} уже занят")
        else:
            print("\nТакого номера нет")
        
    def unbook(self, room):
        if room in self.rooms:
            if self.rooms[room] == False:
                self.rooms[room] = True
                print(f"\nКомната {room} разбронирована")
            else:
                print(f"\nНомер {room} не занят")
        else:
            print("\nТакого номера нет")
        
hotel1 = Hotel("Отель 'Тихий Ден'")
while True:
    user = input("\n[1] - Информация об отеле\n[2] - Забронировать номер\n[3] - Снять бронь с номера\n[4] - Выход\n")
    if user == "1":
        hotel1.info()
    elif user == "2":
        hotel1.book(int(input("Введите номер для брони: ")))
    elif user == "3":
        hotel1.unbook(int(input("Введите номер для снятия брони: ")))
    elif user == "4":
        break
    else:
        print("Неверный ввод")
