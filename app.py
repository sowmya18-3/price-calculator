def calculate_final_price(unit_price, quantity, discount_percent, tax_percent):
    subtotal = unit_price * quantity
    discount_amount = subtotal * discount_percent / 100
    discounted_total = subtotal - discount_amount
    tax_amount = discounted_total * tax_percent / 100
    final_price = discounted_total + tax_amount
    return round(final_price, 2)


print(calculate_final_price(45.88, 9, 18, 9.7))