from forex_python.bitcoin import BtcConverter
from datetime import date, time   # import the date module from datetime library


def forex_BTC():
    """Get latest price of one Bitcoin"""
    b = BtcConverter()   # add "force_decimal=True" parmeter to get Decimal rates
    current_date = date.today()   # call the date function from the date module
    current_time = time()
    user_input = input("Enter the currency code: ").upper()
    currency_price = b.get_latest_price(user_input)
    print(f"The {user_input} Bitcoin price as of {current_date} at {current_time} is: {currency_price}")