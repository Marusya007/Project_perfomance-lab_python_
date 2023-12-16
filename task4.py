import sys


def min_moves(nums):
    mean_value = sum(nums) // len(nums)
    moves = sum(abs(num - mean_value) for num in nums)
    return moves


if __name__ == "__main__":
    # Проверяем, что передан файл в качестве аргумента командной строки
    if len(sys.argv) != 2:
        print("Использование: python task4.py <input_file>")
        sys.exit(1)

    # Получаем данные из файла
    with open(sys.argv[1]) as input_file:
        nums = [int(line.strip()) for line in input_file]

    # Вычисляем минимальное количество ходов
    result = min_moves(nums)

    # Выводим результат в консоль
    print(result)
