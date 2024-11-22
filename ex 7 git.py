#Задание 1
def create_car(brand: str, color: str, max_speed: int):
    return f"Марка: {brand} Цвет: {color} Максимальная скорость: {max_speed} км/ч"
car_info = create_car("Mercedes", "Черный", 350)
print(car_info)

#Задание 2
def switch_check(switch):
    if switch is True:
        print("True работает")
    elif switch is False:
        print("False не работает")
    else:
        print(f"{switch} сломан.")
switch_1 = True
switch_2 = False
switch_3 = None
switch_check(switch_1)
switch_check(switch_2)
switch_check(switch_3)

#Задание 3
def triangle_type(side1: float, side2: float, side3: float) -> None:
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        if side1 == side2 == side3:
            print("Равносторонний треугольник")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("Равнобедренный треугольник")
        else: 
            print("Разносторонний треугольник")
    else: 
        print("Некорректные стороны. Невозможно построить треугольник.")
triangle_type(3, 3, 3)
triangle_type(5, 5, 8)
triangle_type(3, 4, 5)
triangle_type(1, 2, 3)