import os
import pickle
from utilities import Utility


class ExchangeRateCache:
    """Class for exchange rate cache"""

    @staticmethod
    def getExchangeRates(baseCurrency):
        """Returns current exchange rate (if cache exists) or None (if it does not)"""

        if ExchangeRateCache.checkIfFileExists(baseCurrency):
            cachedResponse = ExchangeRateCache.loadCachedResponse(baseCurrency)
            if ExchangeRateCache.isUpToDate(cachedResponse):
                return cachedResponse['rates']
            else:
                return None
        else:
            return None

    @staticmethod
    def updateCache(baseCurrency, apiResponse):
        """Updates cache file"""
        cacheFile = Utility.createFileName(baseCurrency)
        apiResponse['date'] = Utility.currentDate()
        with open(cacheFile, "wb") as file:
            pickle.dump(apiResponse, file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def loadCachedResponse(baseCurrency):
        """Returns the content of a cache file"""
        cacheFile = Utility.createFileName(baseCurrency)
        with open(cacheFile, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def checkIfFileExists(baseCurrency):
        """Checks if a cache file for a given base already exists"""
        cacheFile = Utility.createFileName(baseCurrency)
        return os.path.isfile(cacheFile)

    @staticmethod
    def isUpToDate(cacheFile):
        """Checks if a cache file is up to date"""
        currentDate = Utility.currentDate()
        if currentDate == cacheFile['date']:
            return 1
        else:
            return 0





