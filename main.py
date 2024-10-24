import random

# Размер игрового поля
FIELD_SIZE = 5

# Создаем игровое поле
field = [[0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

def place_ships(field, num_ships):
    ships_placed = 0
    while ships_placed < num_ships:
        x = random.randint(0, FIELD_SIZE - 1)
        y = random.randint(0, FIELD_SIZE - 1)
        if field[x][y] == 0:  # Если клетка пустая
            field[x][y] = 1  # Размещаем корабль
            ships_placed += 1

place_ships(field, 2)

def shoot(field, x, y):
    if field[x][y] == 1:  # Если попали в корабль
        field[x][y] = 2  # Обновляем ячейку, чтобы показать попадание
        return "Попадание!"
    elif field[x][y] == 0:  # Если промах
        field[x][y] = -1  # Обновляем ячейку, чтобы показать промах
        return "Промах!"
    else:
        return "Эта клетка уже была обстреляна!"

while True:
    print("Текущее состояние игрового поля:")
    for row in field:
        print(row)

    x = int(input("Введите координату X (0-4): "))
    y = int(input("Введите координату Y (0-4): "))

    if 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE:
        result = shoot(field, x, y)
        print(result)

        # Проверка. Закончилась ли игра
        if all(cell != 1 for row in field for cell in row):
            print("Поздравляем! Вы потопили все корабли!")
            break
    else:
        print("Некорректные координаты. Попробуйте снова.")
