from data.requests_data import requests
import json

with open("data/requests.json", "w", encoding="utf-8") as file:
    json.dump(requests, file, ensure_ascii=False, indent=2)

with open("data/requests.json", "r", encoding="utf-8") as file:
    load_requests = json.load(file)


print(f"Кол-во загруженых сообщений: {len(load_requests)}")
print(f"Текст первого сообщения: {load_requests[0]['text']}")

for load_request in load_requests:
    print(load_request['category'])
