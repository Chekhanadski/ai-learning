requests = [
  {
    'id': 1,
    'text': 'hello',
    'category': 'general',
    'status': 'new',
    'rating': 3
  },

  {
    'id': 2,
    'text': 'не могу войти в аккаунт',
    'category': 'technical',
    'status': 'processed',
    'rating': 2
  },

    {
    'id': 3,
    'text': 'проблема с оплатой телефона',
    'category': 'billing',
    'status': 'new',
    'rating': 4
  },

    {
    'id': 4,
    'text': 'как украсть миллион',
    'category': 'general',
    'status': 'rejected',
    'rating': 0
  },

    {
    'id': 5,
    'text': 'получил ошибку 414',
    'category': 'technical',
    'status': 'processed',
    'rating': 5
  },
]


# Часть 1. Все обращения

print("All requests:")

for request in requests:
    print(f"id: {request['id']}")
    print(f"category: {request['category']}")
    print(f"status: {request['status']}")
    print("")


# Часть 2. Общая статистика

print(f"Total requests: {len(requests)}")

status_new = 0

for request in requests:
    if request['status'] == 'new':
        status_new = status_new + 1

print(f"New requests: {status_new}")

sum_rating = 0

for request in requests:
    sum_rating = sum_rating + request["rating"]

print(f"Average rating: {sum_rating / len(requests)}")


# Часть 3. Технические обращения

for request in requests:
    if request['category'] == 'technical':
        print(f"Id: {request['id']}")
        print(f"Text: {request['text']}")
        print(f"Rating: {request['rating']}")


# Часть 4. Распределение по рейтингу

for request in requests:
    if request['rating'] in [4, 5]:
        print(f"ID {request['id']} - well processed")
    elif request['rating'] == 3:
        print(f"ID {request['id']} - normal result")
    elif request['rating'] == 0:
        print(f"ID {request['id']} - no rating")
    else:
        print(f"ID {request['id']} - requires review")


# Часть 5. Фильтр по категории

selected_category = input(
    "Enter category (technical, billing, general): "
)

category_found = ""

for request in requests:
    if selected_category == request['category']:
        category_found = 'found'
        print(f"ID: {request['id']}")
        print(f"Text: {request['text']}")
        print(f"Status: {request['status']}")

if category_found != 'found':
    print("No requests found for this category.")
