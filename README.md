# KiwiRate Currency Converter
This is a simple Currency Converter CLI and web API application implemented in Python3.5. 

**KiwiRate supports the following currencies:**</br> 

|Code|Symbol|Country name|Code|Symbol|Country name|
| --- | --- | --- | --- | --- | --- |
|AUD|*not supported*|Australia Dollar|JPY|*not supported*|Japan Yen|
|BGN|лв|Bulgaria Lev|KRW|₩|South Korea Won|
|BRL|R$|Brazil Real|MXN|*not supported*|Mexico Peso|
|CAD|*not supported*|Canada Dollar|MYR|RM|Malaysia Ringgit|
|CHF|CHF|Switzerland Franc|NOK|*not supported*|Norway Krone|
|CNY|¥|China Yuan Renminbi|NZD|*not supported*|New Zealand Dollar|
|CZK|Kč|Czech Republic Koruna|PHP|₱|Philippines Piso|
|DKK|kr|Denmark Krone|PLN|zł|Poland Zloty|
|EUR|€|Euro Member Countries|RON|lei|Romania Leu|
|GBP|£|United Kingdom Pound|RUB|₽|Russia Ruble|
|HKD|*not supported*|Hong Kong Dollar|SEK|*not supported*|Sweden Krona|
|HRK|kn|Croatia Kuna|SGD|*not supported*|Singapore Dollar|
|HUF|Ft|Hungary Forint|THB|฿|Thailand Baht|
|IDR|Rp|Indonesia Rupiah|TRY|₺|Turkey Lira|
|ILS|₪|Israel Shekel|USD|$|United States Dollar|
|INR|₹|India Rupee|ZAR|R|South Africa Rand|

## Required Packages
See the `requirements.txt` file.

## Fixer API Reference
This project makes use of the [Fixer API](http://fixer.io/) to get currency exchange rates. It provides the latest official rates published by the [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html). The reference rates are usually updated around 4PM CET on every working day.

An example query to get the EUR exchange rate looks like:

  `https://api.fixer.io/latest?base=EUR`

#### Note
The conversion rates are cached to reduce server load.
  
## Flask Framework Reference
This project also makes use of the web framework [Flask](http://flask.pocoo.org/). Parameters `host` and `port` are set to default values: `127.0.0.1` and `5000` respectively. 

## Output Format
JSON with following structure:
```
{
  "input": {
    "amount": <float value>, 
    "currency": <a three letter input currency code>
  }, 
  "output": {
    <a three letter output currency code>: <float value>
  }
}
```
## API Error Output Format
JSON with following structure

```
{
  "error_code": <error code>, 
  "error_message": <error message>
}
```

## Usage

### CLI Application
See the implementation: `currency_converter.py`

     ./currency_converter.py [--amount <value>] --input_currency <currencyCode_or_Symbol> [--output_currency <currencyCode_or_Symbol>]
#### Parameters
The order of parameters does not matter.<br/>

|Name|Required|Description|Example|
| --- | --- | --- | --- |
|`amount` |*optional*| the amount which we want to convert (float). Default value is 1.0| 100 |
|`input_currency` |*required*| a three letter base currency code or a base currency symbol| CAD |
|`output_currency` |*optional*| a three letter requested output currency code or a requested output currency symbol. If this parameter is missing, the KiwiRate performs the conversion to all supported currencies| Kč |  

#### Example 
Input: </br>
`./currency_converter.py --amount 15 --input_currency $ --output_currency EUR`</br>
</br>Output:
```
{
  "input": {
    "amount": 15.0, 
    "currency": "USD"
  }, 
  "output": {
    "EUR": 12.06
  }
}
```
Input: </br>
`./currency_converter.py --amount 9 --input_currency zł`</br>
</br>Output:
```
{
  "input": {
    "amount": 9.0, 
    "currency": "PLN"
  }, 
  "output": {
    "AUD": 3.34, 
    "BGN": 4.25, 
    "BRL": 8.51, 
    "CAD": 3.33,
    ...
    "USD": 2.7, 
    "ZAR": 32.13
  }
}
```
Input: </br>
`./currency_converter.py --input_currency € --output_currency PLN`</br>
</br>Output:
```
{
  "input": {
    "amount": 1.0, 
    "currency": "EUR"
  }, 
  "output": {
    "PLN": 4.14
  }
}
```

### Web API Application
See the implementation: `currency_converter_API.py`

**BaseURL**
          
    GET http://127.0.0.1:5000/currency_converter
    
#### Parameters
The following URL encoded parameters are accepted:

|Name|Required|Description|Example|
| --- | --- | --- | --- |
|`amount` |*optional*| the amount which we want to convert (float). Default value is 1.0| 2.5 |
|`input_currency` |*required*| a three letter base currency code or a base currency symbol| EUR |
|`output_currency` |*optional*| a three letter requested output currency code or a requested output currency symbol. If this parameter is missing, the KiwiRate performs the conversion to all supported currencies| $ |  

#### Example 
Input: </br>
`GET /currency_converter?amount=10&output_currency=czk&input_currency=€ HTTP/1.1`</br>
</br>Output:
```
{
  "input": {
    "amount": 10.0, 
    "currency": "EUR"
  }, 
  "output": {
    "CZK": 253.57
  }
}
```
Input: </br>
`GET /currency_converter?amount=1000.25&input_currency=HUF HTTP/1.1`</br>
</br>Output:
```
{
  "input": {
    "amount": 1000.25, 
    "currency": "HUF"
  }, 
  "output": {
    "AUD": 4.97, 
    "BGN": 6.31, 
    "BRL": 12.64, 
    "CAD": 4.95,
    ...
    "USD": 4.02, 
    "ZAR": 47.75
  }
}
```
Input: </br>
`GET /currency_converter?input_currency=CAD&output_currency=USD HTTP/1.1`</br>
</br>Output:
```
{
  "input": {
    "amount": 1.0, 
    "currency": "CAD"
  }, 
  "output": {
    "USD": 0.81
  }
}
```
