#!/usr/bin/python3.5
import sys

from exchange_rate import ExchangeRateAPI
from create_output import JsonCreator
from currencies import Currencies
from cmd_args_parser import CmdParser
from exceptions import *
from utilities import Utility


class CurrencyConverter:
    """This class performs the requested conversion"""

    @staticmethod
    def getConversion(inputCurrency, outputCurrencies, amount) -> dict:
        """Returns the result of requested conversion"""

        conversion = dict()
        exchangeRateService = ExchangeRateAPI()

        for outputCurrency in outputCurrencies:

            if outputCurrency == inputCurrency:
                conversion[outputCurrency] = amount
                return conversion

            rate = exchangeRateService.getExchangeRate(inputCurrency, outputCurrency)
            totalValue = amount*float(rate)
            conversion[outputCurrency] = round(totalValue, 2)

        return conversion


def main():

    try:
        args = CmdParser.parseArguments()

        inputCurrency = Currencies.getCurrencyCode(args['input'])
        outputCurrency = args['output']
        amount = args['amount']

        conversion = CurrencyConverter.getConversion(inputCurrency, outputCurrency, amount)

        printResults = JsonCreator.finalOutput(inputCurrency, conversion, amount)
        print(printResults)

    except InvalidArgumentError as invArgErr:
        Utility.errorStatement(invArgErr.message)
    except RequestError as reqErr:
        sys.stderr.write(reqErr.message)
        sys.exit()


if __name__ == '__main__':
    main()


