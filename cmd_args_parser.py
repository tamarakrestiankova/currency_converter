import copy
import getopt
import sys

from currencies import Currencies
from utilities import Utility
from exceptions import *


class CmdParser:
    """Class for parsing and obtaining data from the command line"""

    @staticmethod
    def parseArguments() -> dict:
        """Parses the command line arguments"""

        conversionAmount = -1
        inputCurrency = None
        outputCurrencies = [None]

        if len(sys.argv) == 1:
            print(Utility.help())
            sys.exit()

        try:
            optlist, args = getopt.getopt(sys.argv[1:], 'h', ['amount=', 'input_currency=', 'output_currency=', 'help'])
        except getopt.GetoptError:
            raise InvalidArgumentError("Oops, it looks like you entered an invalid option.")

        if not len(args) == 0:
            raise InvalidArgumentError("Oops, it looks like you entered an invalid option.")

        for option, argument in optlist:
            if option in ('-h', '--help'):
                print(Utility.help())
                sys.exit()

            elif option in '--amount':
                if conversionAmount is not -1:
                    raise InvalidArgumentError("Please select only one amount, output or input currency.")
                conversionAmount = argument

            elif option in '--input_currency':
                if inputCurrency is not None:
                    raise InvalidArgumentError("Please select only one amount, output or input currency.")
                inputCurrency = argument

            elif option in '--output_currency':
                if not None in outputCurrencies:
                    raise InvalidArgumentError("Please select only one amount, output or input currency.")
                outputCurrencies = [argument]

        Utility.checkArguments(inputCurrency, conversionAmount)
        inputCurrency = Currencies.getCurrencyCode(inputCurrency)
        conversionAmount = abs(float(conversionAmount))

        if None not in outputCurrencies:
            outputCurrencies = [Currencies.getCurrencyCode(outputCurrencies[0])]

        else:
            outputCurrencies = copy.copy(Currencies.listOfCurrencies)
            outputCurrencies.remove(inputCurrency)

        return {'amount': conversionAmount,
                'input': inputCurrency,
                'output': outputCurrencies}
