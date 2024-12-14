def convert_to_euro(amount_in_dollars):
    dollar_to_euro_rate = 0.85
    return amount_in_dollars * dollar_to_euro_rate

def demo_refact(money_net): 
    tax_rate = 0.3
    money_after_tax = money_net * (1 - tax_rate)

    money_in_euro = convert_to_euro(money_after_tax)

    return money_in_euro

net_income = 1
money_in_euro = demo_refact(net_income)
print(f"\nMoney in $ before tax: {net_income}")
print(f"\nMoney in Euro after tax: {money_in_euro:.2f}")
