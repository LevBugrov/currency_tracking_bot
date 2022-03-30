import json
from os.path import exists


class Database:
    def __init__(self):
        if not exists('data.json'):
            my_file = open("data.json", "w")
            my_file.write(r'{"jpy": "1 yen is equal to  rubles"}')
            my_file.close()
            self.data = dict()
        else:
            with open('data.json', 'r') as f:
                self.data = json.load(f)

    def get_data(self, currency_name, get_price):
        return self.data[currency_name][:-7] + get_price(currency_name) + self.data[currency_name][-7:]

    def update_data(self):
        with open('data.json', 'w') as f:
            f.write(json.dumps(self.data))
        with open('data.json', 'r') as f:
            self.data = json.load(f)

    def add_currency(self, currency_name, currency):
        add_cur = ''
        try:
            add_cur = currency.get_currency_price(currency, currency_name)
        except:
            return f'Не получилось найти валюту под названием ({currency_name})'

        if add_cur:
            self.data[currency_name] = f"1 {currency_name} is equal to  rubles"
            self.update_data()
            return f'валюта {currency_name} добавлена!'

    def delete_currency(self, currency_name, password):
        if password == '4321' and self.data.get(currency_name):
            del self.data[currency_name]
            with open('data.json', 'w') as f:
                f.write(json.dumps(self.data))
            return "Валюта "+currency_name+' удалена.'
        else:
            return 'Что-то пошло не так...'

    def change_cur(self, old_cur, new_curr, password):
        if password == '4321' and self.data.get(old_cur):
            del self.data[old_cur]
            self.data[new_curr] = f"1 {new_curr} is equal to  rubles"
            with open('data.json', 'w') as f:
                f.write(json.dumps(self.data))
            return 'Валюта ' + old_cur + ' изменена на ' + new_curr
        else:
            return 'Что-то пошло не так...'

    def all_currency(self):
        return "\n".join(self.data.keys())
