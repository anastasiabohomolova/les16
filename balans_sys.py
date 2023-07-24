import json

with open("users_base.json", 'r') as file:
    data = json.load(file)
    l = []
    for v in data.values():
        n = v['balans']
        l.append(n)

    sum_balansy_sys = sum(l)
    if sum_balansy_sys < 300000:
        print("Поповніть банкомат готівкою")

    with open("balans_bank.txt", 'w') as file:
        file.write(str(sum_balansy_sys))






