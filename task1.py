import sys


def circular_array_path(n, m):
    # Создаем круговой массив
    circular_array = list(range(1, n + 1))

    # Инициализируем путь
    path = []

    # Начинаем с первого элемента
    current_index = 0

    # Перебираем круговой массив
    for _ in range(n):
        # Добавляем текущий элемент к пути
        path.append(circular_array[current_index])

        # Переходим к следующему элементу с шагом m
        current_index = (current_index + m - 1) % n

    return path


if __name__ == "__main__":
    # Проверяем, что передано два аргумента командной строки
    if len(sys.argv) != 3:
        print("Использование: python script.py <n> <m>")
        sys.exit(1)

    # Получаем значения n и m из аргументов командной строки
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    # Получаем путь и выводим результат
    result = circular_array_path(n, m)
    print("".join(map(str, result)))
