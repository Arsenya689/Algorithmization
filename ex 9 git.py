#Задание 1
class CreateCharacter:
    def __init__(self, character_name: str, character_class: str, character_health: int, character_damage: int):
        self.name = character_name
        self.cclass = character_class
        self.health = character_health
        self.damage = character_damage

    def info(self):
        print(f"Имя: {self.name}\nКласс: {self.cclass}\nЗдоровье: {self.health}\nУрон: {self.damage}\n")

    def trip_start(self):
        print(f"Персонаж {self.name} отправился в путешествие и пока недоступен.\n")

    def trip_end(self):
        print(f"Персонаж {self.name} возвращается назад.\n")

    def train(self):
        print(f"Персонаж {self.name} начал тренировку. Некоторое время он не будет доступен, однако станет сильнее!\n")
        self.health += 10
        self.damage += 5

    def battle(self):
        print(
            f"Персонаж {self.name} хочет начать сражаться!\nЕго показатели: Жизни: {self.health} и урон: {self.damage}\n")


pers_1 = CreateCharacter("Игорь", "Боец", 99, 15)
pers_1.info()
pers_1.trip_start()
pers_1.trip_end()
pers_1.train()
pers_1.info()
pers_1.battle()

#Задание 2
class Room:

    def __init__(self, name):
        self.name = name
        self.items = []

    def print_items(self):
        print(f"Все предметы в комнате {self.name}: {', '.join(self.items)}")

    def add_item(self, *item):
        self.items.extend(item)

    def del_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Все предметы в комнате: {', '.join(self.items)}")
        else:
            print("Такого предмета нет в комнате")

    def find_item(self, item):
        if item in self.items:
            print("Такой предмет есть в комнате")
        else:
            print("Такого предмета нет в комнате")

    def count_items(self):
        print(f"В комнате {len(self.items)} предметов")

    def clear_items(self):
        self.items = []

    def replace_item(self, old_item, new_item):
        if old_item in self.items:
            self.items.remove(old_item)
            self.items.append(new_item)
            print(f"Предмет {old_item} заменён на {new_item}")
        else:
            print("Такого предмета нет в комнате")

    def move_item_to(self, item, another_room):
        if item in self.items:
            self.items.remove(item)
            another_room.items.append(item)
            print(f"Предмет {item} перенесён в {another_room.name}")
        else:
            print("Такого предмета нет в комнате")


room1 = Room("Кухня")
room2 = Room("Ванная")
room1.add_item("Холодильник", "Стул", "Стол")
room1.move_item_to("Холодильник", room2)
room1.print_items()
room2.print_items()

#Задание 3
def isint(var):
    if type(var) == type(1):
        return True
    else:
        return False


class Book:
    def __init__(self, name: str, pages: int, year: int):
        self.name = name
        self.pages = pages
        self.year = year

    def info(self):
        print(f"Название: {self.name}\nКоличество страниц: {self.pages}\nГод издания: {self.year}\n")

    def update_pages(self, pages: int):
        if isint(pages):
            self.pages = pages
        else:
            print("Неверное значение страниц\n")

    def older_than(self, year: int):
        if isint(year):
            if self.year > year:
                print(True)
            else:
                print(False)
        else:
            print("Неверное значение года\n")


book1 = Book("Name1", 200, 2005)
book2 = Book("Name2", 500, 1999)
book1.info()
book1.update_pages(250)
book1.info()
book2.older_than(2000)
