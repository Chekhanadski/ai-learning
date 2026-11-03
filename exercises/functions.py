requests = [
    {
        "id": 1,
        "text": "hello",
        "category": "general",
        "status": "new",
        "rating": 3
    },
    {
        "id": 2,
        "text": "не могу войти в аккаунт",
        "category": "technical",
        "status": "processed",
        "rating": 2
    },
    {
        "id": 3,
        "text": "проблема с оплатой телефона",
        "category": "billing",
        "status": "new",
        "rating": 4
    },
    {
        "id": 4,
        "text": "как украсть миллион",
        "category": "general",
        "status": "rejected",
        "rating": 0
    },
    {
        "id": 5,
        "text": "получил ошибку 414",
        "category": "technical",
        "status": "processed",
        "rating": 5
    },
]


# Request statistics

def count_new_requests(requests):
    new_count = 0

    for request in requests:
        if request["status"] == "new":
            new_count += 1

    return new_count


def average_rating(requests):
    rating_count = 0
    rating_sum = 0

    for request in requests:
        rating_count += 1
        rating_sum += request["rating"]

    return rating_sum / rating_count


# Category analysis

def count_category_requests(requests, category):
    category_count = 0

    for request in requests:
        if request["category"] == category:
            category_count += 1

    return category_count


def get_request_texts_by_category(requests, category):
    request_texts = []

    for request in requests:
        if request["category"] == category:
            request_texts.append(request["text"])

    return request_texts


# Program output

new_count = count_new_requests(requests)
print(f"Count new requests: {new_count}")

average = average_rating(requests)
print(f"Average rating: {average}")

category = input("Enter category: ")

category_count = count_category_requests(requests, category)
print(f"{category} -> {category_count}")

request_texts = get_request_texts_by_category(requests, category)

for request_text in request_texts:
    print(f"{request_text}")