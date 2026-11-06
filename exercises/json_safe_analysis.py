import json

try:
    with open("data/requests.json", "r", encoding="utf-8") as file:
        load_requests = json.load(file)

    category_input = input("Введите категорию: ")
    count_text = 0
    count_rating = 0 

    for load_request in load_requests:
      if load_request['category'] == category_input:
        count_text += 1
        count_rating += load_request['rating']

        print(f"ID: {load_request['id']}")
        print(f"Text: {load_request['text']}")
        print(f"Status: {load_request['status']}")
        print(f"Rating: {load_request['rating']}")

    print(f"Количество найденных обращений: {count_text}")

    if count_text > 0:
        print(f"Средний рейтинг: {count_rating/count_text}")
    else:
        print(f"Категория не найдена")
    

except FileNotFoundError:
    print("Ошибка: файл requests.json не найден.")

except json.JSONDecodeError:
     print("Ошибка: файл содержит некорректный JSON.")
