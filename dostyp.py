import json
from datetime import datetime
class Control:

    def __init__(self):
        self.__data = json.load(open('users_base.json', 'r'))

    def _zn_cach(self):
        for user_data in self.__data.values():
            if pin == user_data.get("pincod"):
                #print(user_data["balans"])
                suma = int(input('Введіть суму: '))
                if suma < user_data["balans"] or 300000:
                    zaluchok = user_data["balans"] - suma
                    user_data["balans"] = zaluchok
                    new_data = self.__data
                    with open("users_base.json", 'w') as file:
                        json.dump(new_data, file)
                    with open('operations_base.txt', 'a', encoding='utf-8') as file:
                        d = {datetime.now(): 'зняття готівки'}
                        file.write(f'\n{str(d)}\n')
                    print(zaluchok)
                else:
                    print('Сума перевищує баланс або ліміт')

    def _pop_cach(self):
        for user_data in self.__data.values():
            if pin == user_data.get("pincod"):
                suma_popovnia = int(input('Введіть суму: '))
                if suma_popovnia < 50000:
                    new_balans = user_data["balans"] + suma_popovnia
                    user_data["balans"] = new_balans
                    new_data = self.__data
                    with open("users_base.json", 'w') as file:
                        json.dump(new_data, file)
                    with open('operations_base.txt', 'a', encoding='utf-8') as file:
                        d = {datetime.now(): 'поповнення рахунку'}
                        file.write(f'\n{str(d)}\n')

                    print(new_balans)
                else:
                    print('Сума перевищує ліміт')

    def _check_pin(self, n):
        for user_data in self.__data.values():
            if n == user_data.get("pincod"):
                print(f'balans {user_data["balans"]}')
                with open('balans_users.txt', 'a') as file:
                    file.write(f' \nuser {user_data["pincod"]} {user_data["balans"]}\n')
                with open('operations_base.txt', 'a', encoding='utf-8') as file:
                    d = {datetime.now(): 'введення пінкоду'}
                    file.write(f'\n{str(d)}\n')

                return True
        return False




pin = int(input('Введіть пінкод: '))

a = Control()

if a._check_pin(pin):
    print("Пінкод вірний. Доступ надано.")

else:
    print("Пінкод невірний")
    pin = int(input('Спробуйте йще раз: '))
    if a._check_pin(pin):
        print("Пінкод вірний. Доступ надано.")
    else:
        print("Пінкод невірний")
        pin = int(input('Спробуйте йще раз: '))
        if a._check_pin(pin):
            print("Пінкод вірний. Доступ надано.")
        else:
            print("Пінкод невірний. Доступ заборонено.")
            raise TypeError









