from data.requests_data import requests
from exercises.request_tools import count_new_requests, average_rating, get_request_texts_by_category

new_count = count_new_requests(requests)

print(f'Count new requests: {new_count}')

print(f"Average rating: {average_rating(requests)}")

category_input = input("Введите категорию: ") 

list_texts = get_request_texts_by_category(requests, category_input)

for list_text in list_texts:
    print(f"{list_text}")