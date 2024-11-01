# Задание 1
#age = int(input())
#if age < 18:
#    print("Вы несовершеннолетний")
#elif age > 18 and age <= 65:
#    print("Вы трудоспособный человек")
#else:
#    print("Вы пенсионер")

# Задание 2
#buy = int(input())
#if buy < 1000:
#    print("Скидка не предоставляется")
#elif buy > 1000 and buy <= 5000:
    
#    print("Скидка 5%")
#else:
#    print("Скидка 10%")

#Задание 3
#n1 = float(input("Первое число "))
#n2 = float(input("Второе число"))
#op= input("Операция(+,-, *, /):")

#if op == "+":
#    res = n1 + n2
#elif op == "-":
#    res = n1 - n2
#elif op == "*":
#    res = n1 * n2
#elif op == "/":
#    if n2 == 0:
#        print("Ошибка: деление на ноль(тупой)")
#    else:
#        res = n1 / n2
#else:
#    print("Ошибка: неверная операция")

#print(f"{n1} {op} {n2} = {res}")

#Задание 5
#password_correct = '123456789'
#while True:
#    password = input("Введите пароль:")

#    if password == password_correct:
#        print("Верный пароль. Вход разрешен.")
#        break
#    else:
#        print("Пароль неправильный. Попробуйт ёщё раз...")

# Задание 6 
#ans = input()
#green_popug = ("B2", "B4", "B6", "B8", "C2", "C7", "C10", "C11")
#blue_popug = ("B1", "B3", "B7", "C1", "C4", "C5", "C6", "C8", "C9")
#if ans in green_popug:
#    print("Зелёный попугай")
#elif ans in blue_popug:
#    print("Синий попугай")
#else:
#   print("Серый попугай")

# Задание 7
#n = int(input("Введите числа n:"))
#k = int(input("Введите числа k:"))
#if k != 0 and n % k == 0:
#    print(f"{n} кратно {k}")
#else:
#    print(f"{n} не кратно {k} или k равно 0")

#Задание 8
#def check_player_status(level, health):
#    if level < 0 or health < 0 or health > 100:
#        return "Некорректные данные."
#    if level < 5:
#        return "Ваш уровень слишком низкий для выполнения миссии."
#    if health > 50:
#        return "Вы готовы к миссии!"
#    elif 20 <= health <= 50:
#        return "Ваше здоровье низкое, будьте осторожны."
#    else:  # здоровье < 20
#        return "Ваше здоровье слишком низкое для выполнения миссии."
        
#player_level = int(input("Введите уровень игрока: "))
#player_health = int(input("Введите количество здоровья игрока: "))
#message = check_player_status(player_level, player_health)
#print(message)

# Задание 9
#inventory = ["яблоко", "шариковая ручкая"]
#if "ключ" in inventory and "фонарь" in inventory:
#    print("Вы можете пройти через дверь.")
#elif "ключ" not in inventory:
#    print("У вас нет ключа, вы не можете открыть дверь")
#elif "фонарь" not in inventory:
#    print("У вас нет фонаря, слишком темно, чтобы пройти")
#else:
#    print("У вас нет ни ключа, ни фонаря, вы не можете пройти через дверь.")

#Задание 10
#king = "Enemies are coming! Are the archers ready?"
#warrior = "For the Alliance!"
#magician = "The spell is ready."
#if "?" in king or "!" in king:
#    print("Есть одно из них в словах короля")
#elif "?" in warrior or "!" in warrior:
#    print("Есть одно из них в словах воина")
#elif "?" in magician or "!" in magician:
#    print("Есть одно из них в словах мага")
#else:
#    print("alo")

