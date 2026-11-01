persons = [
    {
        'id': 1,
        'last name': 'Chekhanadski',
        'age': 41
    },

    {
        'id': 2,
        'last name': 'Kolen',
        'age': 16
    },

    {
        'id': 3,
        'last name': 'Nakvas',
        'age': 34
    },
]

for person in persons:
     print(f"Id: {person['id']}")
     print(f"Category: {person['last name']}")
     print(f"Status: {person['age']}")
