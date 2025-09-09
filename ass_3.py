def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        amount = (discount_percent / 100) * price
        final_price = price - amount
        return final_price
    else:
        return price

initial_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))
final_price = calculate_discount(initial_price, discount)

if discount >= 20:
    print("The final price after", str(discount) + "% discount is:", str(round(final_price, 2))
)
else:
    print("No discount applied. The price remains:", str(round(final_price, 2)))