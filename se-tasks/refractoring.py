import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def convert_currency(amount, rate=0.85):
    return amount * rate


def apply_tax(income, tax_rate=0.3):
    return income * (1 - tax_rate)


def process_conversion(money_net, tax_rate=0.3, conversion_rate=0.85):
    net_after_tax = apply_tax(money_net, tax_rate)
    money_in_euro = convert_currency(net_after_tax, conversion_rate)
    return money_in_euro


def display_conversion_results(original, converted, currency="EUR"):
    logging.info(f"\nMoney before tax: ${original:.2f}")
    logging.info(f"Money after tax in {currency}: €{converted:.2f}")


if __name__ == "__main__":
    net_income = 1
    money_in_euro = process_conversion(net_income)

    display_conversion_results(net_income, money_in_euro)
