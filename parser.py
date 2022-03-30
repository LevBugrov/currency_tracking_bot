import requests
from bs4 import BeautifulSoup


def get_link(currency_name):
    return f'https://www.google.com/search?q={currency_name}+to+ruble'


class Currency:
    # Заголовки для передачи вместе с URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        pass

    def get_currency_price(self, currency_name):
        """returns the exchange rate"""
        full_page = requests.get(get_link(currency_name), headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "data-precision": 2})
        return convert[0].text
