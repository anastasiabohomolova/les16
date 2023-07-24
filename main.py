from dostyp import Control
import balans_sys
from cours import Cours, Perevod

def run():
    while True:
        menu = int(input('Виберіть дію \n'
                        '1. Зняти кошти \n'
                        '2. Поповнити баланс \n'
                        '3. Актуальний курс валют \n'
                        '4. Перевести суму в валюту \n'
                        ))

        if menu == 1:
            s = Control()
            print(s._zn_cach())

        elif menu == 2:
            s = Control()
            print(s._pop_cach())

        elif menu == 3:
            s = Cours()
            print(s.cours())

        elif menu == 4:
            ch_dia = input('Виберіть купівля або продаж: ')
            if ch_dia == 'купівля':
                s = Perevod()
                print(s._kupivlia())
            elif ch_dia == 'продаж':
                s = Perevod()
                print(s._prodag())



f = run()
print(f)

