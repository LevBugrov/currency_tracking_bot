import unittest
from database import Database
from parser import Currency


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Currency()

    def test_get_price(self):
        self.assertEqual(type(self.parser.get_currency_price("usd")), str)


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.parser = Currency
        self.db = Database()
        self.db.data = dict()
        self.db.data['jpy'] = "1 yen is equal to  rubles"
        self.db.update_data()

    def test_all(self):
        self.assertEqual(self.db.all_currency(), 'jpy')

    def test_add(self):
        self.db.add_currency('usd', self.parser)
        self.assertEqual(self.db.all_currency(), 'jpy\nusd')

    def test_del(self):
        self.db.delete_currency('usd', '4321')
        self.assertEqual(self.db.all_currency(), 'jpy')

    def test_change(self):
        self.db.change_cur('jpy', 'usd', '4321')
        self.assertEqual(self.db.all_currency(), 'usd')
        self.db.change_cur('usd', 'jpy', '4321')


if __name__ == '__main__':
    unittest.main()
