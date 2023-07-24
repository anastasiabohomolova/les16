import requests
from bs4 import BeautifulSoup as Bs
from datetime import datetime


class Cours:
    def cours(self):
        url = 'https://privatbank.ua/rates-archive'
        response = requests.get(url)
        html = Bs(response.content, 'html.parser')
        l = []
        l_2 = []
        l_3 = []
        l1 = []
        l2 = []
        l3 = []
        for i in html.select(".courses-currencies"):
            currency_elements = i.select(".currency-pairs > .purchase > span")

            if currency_elements:
                eur = currency_elements[0].text
                l.append(eur)
                usd = currency_elements[1].text
                l_2.append(usd)
                pln = currency_elements[2].text
                l_3.append(pln)

        for i in html.select(".courses-currencies"):
            currency_elements = i.select(".currency-pairs > .sale > span")

            if currency_elements:
                eur = currency_elements[0].text
                l1.append(eur)
                usd = currency_elements[1].text
                l2.append(usd)
                pln = currency_elements[2].text
                l3.append(pln)

        print(f' EUR: купівля: {l[0]}, продаж: {l1[0]}')
        print(f' USD: купівля: {l_2[0]}, продаж: {l2[0]}')
        print(f' PLN: купівля: {l_3[0]},  продаж: {l3[0]}')

        with open('operations_base.txt', 'a', encoding='utf-8') as file:
            d = {datetime.now(): 'перегляд актуального курсу'}
            file.write(f'\n{str(d)}\n')



class Perevod():
    def _kupivlia(self):
        choice_valutu = input('Виберіть валюту: eur, usd, pln: ')
        if choice_valutu == 'eur':
            url = 'https://privatbank.ua/rates-archive'
            response = requests.get(url)
            html = Bs(response.content, 'html.parser')
            l = []
            for i in html.select(".courses-currencies"):
                currency_elements = i.select(".currency-pairs > .purchase > span")
                if currency_elements:
                    eur = currency_elements[0].text
                    l.append(eur)
                    kup_eur = float(l[0])
                    suma_perevody = float(input('Введіть суму: '))
                    suma_eur = suma_perevody / kup_eur
                    print(int(suma_eur))
                    with open("currency_transactions.txt", 'a', encoding='utf-8') as file:
                        file.write(f'\nкупівля євро: сума внесеня= {str(suma_perevody)} отримана сума євро= {str(suma_eur)}\n')
                        file.close()
                        with open('operations_base.txt', 'a', encoding='utf-8') as file:
                            d = {datetime.now(): 'купівля євро'}
                            file.write(f'\n{str(d)}\n')


                    break
        elif choice_valutu == 'usd':
            url = 'https://privatbank.ua/rates-archive'
            response = requests.get(url)
            html = Bs(response.content, 'html.parser')
            l = []
            for i in html.select(".courses-currencies"):
                currency_elements = i.select(".currency-pairs > .purchase > span")
                if currency_elements:
                    usd = currency_elements[1].text
                    l.append(usd)
                    kup_usd = float(l[0])
                    suma_perevody = float(input('Введіть суму: '))
                    suma_usd = suma_perevody / kup_usd
                    print(int(suma_usd))
                    with open("currency_transactions.txt", 'a', encoding='utf-8') as file:
                        file.write(f'\nкупівля долара: сума внесеня= {str(suma_perevody)} отримана сума долара= {str(suma_usd)}\n')
                        file.close()
                    with open('operations_base.txt', 'a', encoding='utf-8') as file:
                        d = {datetime.now(): 'купівля долара'}
                        file.write(f'\n{str(d)}\n')
                    break
        elif choice_valutu == 'pln':
            url = 'https://privatbank.ua/rates-archive'
            response = requests.get(url)
            html = Bs(response.content, 'html.parser')
            l = []
            for i in html.select(".courses-currencies"):
                currency_elements = i.select(".currency-pairs > .purchase > span")
                if currency_elements:
                    pln = currency_elements[2].text
                    l.append(pln)
                    kup_pln = float(l[0])
                    suma_perevody = float(input('Введіть суму: '))
                    suma_pln = suma_perevody / kup_pln
                    print(int(suma_pln))
                    with open("currency_transactions.txt", 'a', encoding='utf-8') as file:
                        file.write(f'\nкупівля злотих: сума внесеня= {str(suma_perevody)} отримана сума злотих= {str(suma_pln)}\n')
                        file.close()
                    with open('operations_base.txt', 'a', encoding='utf-8') as file:
                        d = {datetime.now(): 'купівля злотих'}
                        file.write(f'\n{str(d)}\n')
                    break

    def _prodag(self):
        choice_valutu = input('Виберіть валюту: eur, usd, pln: ')
        if choice_valutu == 'eur':
            url = 'https://privatbank.ua/rates-archive'
            response = requests.get(url)
            html = Bs(response.content, 'html.parser')
            l = []
            for i in html.select(".courses-currencies"):
                currency_elements = i.select(".currency-pairs > .sale > span")
                if currency_elements:
                    eur = currency_elements[0].text
                    l.append(eur)
            pr_eur = float(l[0])
            suma_perevody = float(input('Введіть суму: '))
            suma_eur = suma_perevody * pr_eur
            print(int(suma_eur))
            with open("currency_transactions.txt", 'a', encoding='utf-8') as file:
                file.write(f'\nпродаж євро: сума внесеня= {str(suma_perevody)} отримана сума грн= {str(suma_eur)}\n')
                file.close()
            with open('operations_base.txt', 'a', encoding='utf-8') as file:
                d = {datetime.now(): 'продаж євро'}
                file.write(f'\n{str(d)}\n')

        elif choice_valutu == 'usd':
            url = 'https://privatbank.ua/rates-archive'
            response = requests.get(url)
            html = Bs(response.content, 'html.parser')
            l = []
            for i in html.select(".courses-currencies"):
                currency_elements = i.select(".currency-pairs > .sale > span")
                if currency_elements:
                    usd = currency_elements[1].text
                    l.append(usd)
            pr_usd = float(l[0])
            suma_perevody = float(input('Введіть суму: '))
            suma_usd = suma_perevody * pr_usd
            print(int(suma_usd))
            with open("currency_transactions.txt", 'a', encoding='utf-8') as file:
                file.write(f'\nпродаж долара: сума внесеня= {str(suma_perevody)} отримана сума грн= {str(suma_usd)}\n')
                file.close()
            with open('operations_base.txt', 'a', encoding='utf-8') as file:
                d = {datetime.now(): 'продаж долара'}
                file.write(f'\n{str(d)}\n')

        elif choice_valutu == 'pln':
            url = 'https://privatbank.ua/rates-archive'
            response = requests.get(url)
            html = Bs(response.content, 'html.parser')
            l = []
            for i in html.select(".courses-currencies"):
                currency_elements = i.select(".currency-pairs > .sale > span")
                if currency_elements:
                    pln = currency_elements[2].text
                    l.append(pln)
            pr_pln = float(l[0])
            suma_perevody = float(input('Введіть суму: '))
            suma_pln = suma_perevody * pr_pln
            print(int(suma_pln))
            with open("currency_transactions.txt", 'a', encoding='utf-8') as file:
                file.write(f'\nпродаж злотих: сума внесеня= {str(suma_perevody)} отримана сума грн= {str(suma_pln)}\n')
                file.close()
            with open('operations_base.txt', 'a', encoding='utf-8') as file:
                d = {datetime.now(): 'продаж злотих'}
                file.write(f'\n{str(d)}\n')



c = Cours()
p = Perevod()