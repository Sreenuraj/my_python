class Transaction:

    def __init__(self, amount, date, currency='USD', usd_conversion_rate=1, description=None):
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def description(self):
        return self.__description

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate


class Account:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        self.__transaction = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        assert len(name) > 3, "Account name should be at least 4 char"
        self.__name = name

    @property
    def number(self):
        return self.__number

    def __len__(self):
        return len(self.__transaction)

    def apply(self, transaction):
        return self.__transaction.append(transaction)

    def balance(self):
        total = 0.0
        for transaction in self.__transaction:
            total += transaction.usd
        return total
