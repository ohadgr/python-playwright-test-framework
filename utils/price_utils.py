from decimal import Decimal


def parse_price(price):
    clean_price = price.split()
    return Decimal(clean_price[-1].replace("$", ""))
