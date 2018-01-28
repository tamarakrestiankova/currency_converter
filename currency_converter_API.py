#!flask/bin/python3.5

import copy
from currency_converter import CurrencyConverter
from create_output import JsonCreator
from currencies import Currencies
from utilities import Utility
from exceptions import *

from flask import Flask, request


app = Flask(__name__)


@app.route('/currency_converter', methods=['GET'])
def currencyConverterAPI():
    """This class gets URL parameters and performs the requested conversion."""

    amount = request.args.get('amount', default=1)
    inputCurrency = request.args.get('input_currency')
    outputCurrency = [request.args.get('output_currency')]

    try:
        urlParameters = checkUrlParameters(inputCurrency, outputCurrency, amount)
        conversion = CurrencyConverter.getConversion(urlParameters['input_currency'], urlParameters['output_currency'], urlParameters['amount'])

    except RequestError as reqErr:
        return JsonCreator.jsonErrStructure(reqErr.message, reqErr.code), reqErr.code

    except InvalidArgumentError as invArgErr:
        return JsonCreator.jsonErrStructure(invArgErr.message, invArgErr.code), invArgErr.code

    return JsonCreator.finalOutput(urlParameters['input_currency'], conversion, urlParameters['amount']), 200


def checkUrlParameters(inputCurrency, outputCurrency, amount):
    """Checks if the URL parameters are valid and returns currency
    three letter code representation and a float amount value"""

    Utility.checkArguments(inputCurrency, amount)
    inputCurrency = Currencies.getCurrencyCode(inputCurrency)

    if None not in outputCurrency:
        outputCurrency = [Currencies.getCurrencyCode(outputCurrency[0])]

    if None in outputCurrency:
        outputCurrency = copy.copy(Currencies.listOfCurrencies)
        outputCurrency.remove(inputCurrency)

    amount = abs(float(amount))

    return {'input_currency': inputCurrency,
            'output_currency': outputCurrency,
            'amount': amount}


if __name__ == '__main__':
     app.run(debug=True)




