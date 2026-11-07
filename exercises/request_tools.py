# Подсчёт новых обращений

def count_new_requests(requests):
    new_count = 0

    for request in requests:
        if request['status'] == 'new':
            new_count = new_count + 1

    return new_count

# Средний рейтинг

def average_rating(requests):
    rating_count = 0
    rating_sum = 0

    for request in requests:
        rating_count += 1
        rating_sum += request['rating']

    return rating_sum / rating_count

def get_request_texts_by_category(requests, category):
    text_list = []

    for request in requests:
      if request['category'] == category:
        text_list.append(request['text'])

    return text_list