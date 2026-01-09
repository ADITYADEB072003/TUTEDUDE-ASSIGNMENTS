try:
    order_amount = int(input("Enter order amount: "))

    if order_amount >= 2000:
        discount = 0.15
    elif order_amount >= 1500:
        discount = 0.10
    elif order_amount >= 1000:
        discount = 0.07
    else:
        discount = 0

    discount_amount = order_amount * discount
    subtotal = order_amount - discount_amount
    tax = subtotal * 0.05
    final_total = subtotal + tax

    print(f"Subtotal: {subtotal}")
    print(f"Tax (5%): {tax}")
    print(f"Final Amount: {final_total}")

except ValueError:
    print("Invalid input. Please enter a number.")