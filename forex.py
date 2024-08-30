from forex_python.bitcoin import BtcConverter
from datetime import date, datetime   # import the date and datetime modules from datetime library


def forex_BTC(currency):
    """Get latest price of one Bitcoin"""
    try:
        b = BtcConverter()   # add "force_decimal=True" parmeter to get Decimal rates
        current_date = date.today()   # call the date function from the date module
        current_time = datetime.now().time()
        currency = currency.upper()
        currency_price = b.get_latest_price(currency)
        if currency_price == None:
            return 'Invalid input.  Please check the currency codes and try again'
        return (f"The {currency} Bitcoin price as of {current_date} at {current_time} is: ${currency_price}")
    except ValueError:
        return 'Invalid input.  Please check the currency codes and try again'
        