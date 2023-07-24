import json

users = '''{"user_1":{"pincod": 1234, "balans": 5000}, "user_2":{"pincod": 2535, "balans": 15000}, "user_3":{"pincod": 4557, "balans": 25000}}'''


data = json.loads(users)
with open('users_base.json', 'w') as file:
    json.dump(data, file)






