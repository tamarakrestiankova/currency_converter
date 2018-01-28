from exceptions import InvalidArgumentError


class Currencies:
    """This class contains a list of all supported currencies
    and also maps currency codes if necessary."""

    listOfCurrencies = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK',
                        'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR',
                        'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN',
                        'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

    currencyMapper = {'$': 'USD', 'лв': 'BGN', 'R$': 'BRL', 'Kč': 'CZK', 'kr': 'DKK',
                      'kn': 'HRK', 'Ft': 'HUF', 'Rp': 'IDR', '₹': 'INR', 'RM': 'MYR',
                      '€': 'EUR', '¥': 'CNY', '£': "GBP", '₪': 'ILS', '₩': 'KRW', 'lei': 'RON',
                      '₱': 'PHP', '฿': 'THB', 'zł': 'PLN', '₽': 'RUB', '₺': 'TRY', 'R': 'ZAR'}

    @staticmethod
    def getCurrencyCode (currencyCode):
        """Checks if a given currency is valid and supported by the program.
        If a currency symbol is given instead of three letter currency code,
        the function maps the symbol into the valid currency code."""

        if currencyCode in Currencies.currencyMapper.keys():
            return Currencies.currencyMapper.get(currencyCode)

        else:
            currencyCode = currencyCode.upper()
            if currencyCode not in Currencies.listOfCurrencies:
                raise InvalidArgumentError("The given input/output currency does not exist or it is not supported.")
            else:
                return currencyCode
