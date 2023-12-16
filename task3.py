import json
import sys


def fill_values(tests, values):
    # Создаем словарь для быстрого доступа к значениям тестов по их id
    values_dict = {item['id']: item['value'] for item in values['values']}

    # Рекурсивно заполняем значения в структуре tests
    def fill_test(test):
        test['value'] = values_dict.get(test['id'], '')
        if 'values' in test:
            for subtest in test['values']:
                fill_test(subtest)

    for test_group in tests['tests']:
        fill_test(test_group)


if __name__ == "__main__":
    # Проверяем, что передано два аргумента командной строки
    if len(sys.argv) != 3:
        print("Использование: python task3.py <tests.json> <values.json>")
        sys.exit(1)

    # Получаем данные из файлов
    with open(sys.argv[1]) as tests_file:
        tests_data = json.load(tests_file)

    with open(sys.argv[2]) as values_file:
        values_data = json.load(values_file)

    # Заполняем значения в структуре tests
    fill_values(tests_data, values_data)

    # Записываем результат в файл report.json
    with open('report.json', 'w') as report_file:
        json.dump(tests_data, report_file, indent=2)