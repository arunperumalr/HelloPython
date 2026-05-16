

def calculate_cart_value(cart_items, discount = 0.0):
    # cart_items = { item1:price1,item2:price2...}
    # discount(float) - Discount percentage(default 0%)

    sub_total = float(sum(cart_items.values()))
    discount_amount = discount * sub_total
    final_cart_value = sub_total - discount_amount
    print(f"Cart Subtotal RS. {sub_total}, Discount RS. {discount_amount}, Final Cart Value RS. {final_cart_value}")
    return final_cart_value


cart_value = calculate_cart_value({"apple":1,"orange":2,"berry":3}, 0.1)
print()
print(f"CART VALUE TO PAYMENT GATEWAY: {cart_value}")

