from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

def show_date_time():
    """
    A method for displaying date and time.

    Args: -
    Return: -
    """
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Date and Time: {formatted_date}\n')

def change_currency(price):
    """
    A method for changing price format to local currency

    Args: price (int)
    Return: price with local currency (str)
    """
    return locale.currency(price, grouping=True)

def disc_calculation(percent, amount):
    """
    A method for calculating discount and total amount after discount

    Args:
        - percent (float)
        - amount (int)
    Return: 
        - dictionary of discount and amount after discount
    """
    disc = int(percent * amount)
    new_amount = amount - disc
    return {"discount": disc, "amount after discount": new_amount}

def find_index(cart, name):
    """
    A method for searching for index of an item in the cart.
    Args:
        name (str)
    return
        index (int) of the item if available otherwise return -1
    """
    for item in cart:
        if item["name"].lower() == name.lower():
            return cart.index(item)
    return -1 