#function

def calculate_discount(price, discount_percent):
    return price * discount_percent / 100

price =float(input("Enter the price"))
discount_percent =int(input("Enter the discount percentage"))


if discount_percent >=20:
       print("The final price is: " + str(calculate_discount(price, discount_percent)))

else:
      print("The original price: " + str(price))
