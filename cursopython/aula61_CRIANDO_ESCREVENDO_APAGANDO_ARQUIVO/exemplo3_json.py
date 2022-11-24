import json

d1 = {
    'Pessoa 1': {
        'Nome': 'Luiz',
        'Idade': 25,
    },
    'Pessoa 2': {
        'Nome': 'Rogéria',
        'Idade': 25,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
