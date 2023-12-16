import json

# Открываем файл с тестовыми данными
with open("tests.json") as file:
    data = json.load(file)

print(data)

# Открываем файл с другими данными
with open("values.json") as file:
    data2 = json.load(file)

print(data2)
