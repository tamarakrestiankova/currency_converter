import requests
import json

from exchange_rate_cache import ExchangeRateCache
from exceptions import *


class ExchangeRateAPI:
    """Wrapper class for exchange rate API"""

    BASE_URL = 'https://api.fixer.io/latest'

    def getExchangeRate(self, inputCurrency, outputCurrency) -> float:
        """Returns exchange rates for input currency to output currency"""

        exchangeRates = ExchangeRateCache.getExchangeRates(inputCurrency)

        if exchangeRates is None:

            try:
                urlParams = {'base': inputCurrency}
                response = requests.get(url=self.BASE_URL, params=urlParams)
            except requests.exceptions.Timeout:
                raise RequestError("The request timed out while trying to connect to the remote server.", 408)
            except requests.exceptions.ConnectionError:
                raise RequestError("A connection error occurred.", 503)
            except requests.exceptions.HTTPError:
                raise RequestError("Sorry, an unknown ExchangeRateAPI error occured.", 500)

            if response.status_code is 200:
                responseData = json.loads(response.text)
                exchangeRates = responseData['rates']
            else:
                raise RequestError("Sorry, an unknown ExchangeRateAPI error occured.", 500)

            ExchangeRateCache.updateCache(inputCurrency, responseData)

        return exchangeRates[outputCurrency]







