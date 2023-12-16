import sys
import math
import os


def read_circle_data(file_path):
    with open(file_path) as file:
        line = file.readline().split()
        if len(line) != 3:
            raise ValueError(f"Неверное количество значений в файле {file_path}. Ожидается 3, получено {len(line)}")
        x, y, radius = map(float, line)
    return x, y, radius


def read_points(file_path):
    with open(file_path) as file:
        points = [tuple(map(float, line.split())) for line in file]
    return points


def point_position_relative_to_circle(point, circle):
    x, y = point
    cx, cy, radius = circle
    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)

    if math.isclose(distance, radius):
        return 0  # Точка лежит на окружности
    elif distance < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности


if __name__ == "__main__":
    # Проверяем, что передано два аргумента командной строки
    if len(sys.argv) != 3:
        print("Использование: python task2.py <файл_окружности> <файл_точек>")
        sys.exit(1)

    # Получаем данные окружности и точки из аргументов командной строки
    circle_data = read_circle_data(sys.argv[1])
    points = read_points(sys.argv[2])

    # Определяем положение каждой точки относительно окружности
    for point in points:
        position = point_position_relative_to_circle(point, circle_data)
        print(position)

print(os.getcwd())
