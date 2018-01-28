#!/usr/bin/python3.5
import datetime
import sys
import os

from exceptions import *


class Utility:
    """Offers some handy methods"""

    @staticmethod
    def help():
        """Prints out usage and information about program"""

        return ("\nUsage:\n"
                "\n"
                "./currency_converter.py [--amount <value> ] "
                "--input_currency <currency_code_or_symbol> "
                "[--output_currency <currency_code_or_symbol>]\n"
                "\n"
                "amount <value>.................................amount which you want to convert. Default value is 1.\n"
                "input_currency <currency_code_or_symbol>.......a base currency which you want to convert represented\n"
                "                                               by three letter currency code or currency symbol.\n"
                "output_currency <currency_code_or_symbol>......a requested currency represented by three letter\n"
                "                                               currency code or currency symbol\n"
                "\n"
                "The program supports following currencies: \n"
                "AUD, BGN (лв), BRL (R$), CAD, CHF, CNY (¥), CZK (Kč), DKK (kr), EUR (€),\n"
                "GBP (£), HKD, HRK (kn), HUF (Ft), IDR (Rp), ILS (₪), INR (₹), JPY, KRW (₩),\n"
                "MXN, MYR (RM), NOK, NZD, PHP (₱), PLN (zł), RON (lei), RUB (₽)', SEK, SGD, THB (฿),\n"
                "TRY (₺), USD ($), ZAR (R)\n")


    @staticmethod
    def errorStatement(error):
        """Prints out error message"""

        sys.stderr.write(error)
        print(Utility.help())
        sys.exit()


    @staticmethod
    def isNumber(number):
        """Checks if a given value is a number"""

        try:
            float(number)
            isNumber = True
        except:
            isNumber = False

        return isNumber


    @staticmethod
    def checkArguments(inputCurrency, conversionAmount):
        """Checks if a given input currency and amount are valid."""

        if inputCurrency is None:
            raise InvalidArgumentError("Please, enter a currency you would like to convert.")

        if not Utility.isNumber(conversionAmount):
            raise InvalidArgumentError("Given amount is not a number. Please insert a valid amount.")


    @staticmethod
    def currentDate():
        """Returns current date in format YYYY-MM-DD"""
        return datetime.datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def createFileName(base):
        """Creates and returns a cache file name"""
        pathToCacheFiles = os.getcwd()
        if not os.path.exists('cache'):
            os.makedirs(pathToCacheFiles + '/cache')
        cacheFile = pathToCacheFiles + '/cache/' + base + '.json'
        return cacheFile



