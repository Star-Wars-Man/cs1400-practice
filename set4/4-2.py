total_order_amount = float(input("Enter the total order amount: "))
customer_location = input("Enter the customer location (local, international): ").lower()

if total_order_amount >= 50:
    if customer_location == "local":
        print("Shipping: Free")

elif total_order_amount < 50:
    if customer_location == "local":
        print("Shipping: $5")

elif customer_location == "international":
    print("Shipping: $20")

else:
    print("Invalid input.")