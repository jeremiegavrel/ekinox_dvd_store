import argparse

BTTF_FILMS = [
    "Back to the Future 1",
    "Back to the Future 2",
    "Back to the Future 3",
]

BASE_PRICE = 20
BTTF_DISCOUNT = [15, 13.5, 12]


def compute_price_with_bttf_discount(dvd_list):
    """Applies the BTTF discounts and compute the total price of the cart.

    :param list dvd_list: the titles of all individual DVS in the cart
    :return: the total price of the cart.
    :rtype int
    """

    discounts = {
        film: False for film in BTTF_FILMS
    }
    total = 0
    discounted_dvds = 0

    for dvd in dvd_list:
        if dvd in discounts:
            discounted_dvds += 1
            discounts[dvd] = True
        else:
            total += BASE_PRICE

    if discounted_dvds > 0:
        discount_tier = sum(discounts.values()) - 1
        discount_price = BTTF_DISCOUNT[discount_tier]
        total += discounted_dvds * discount_price

    return total
