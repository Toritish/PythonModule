def calculate_discount():
    price=float(input("input the price:"))
    discount_percent=float(input("Enter the discount:"))
     
    if discount_percent >= 20:
           discount=(20/100)*price
           print(price-discount)
    else:
         print(price)      

calculate_discount()          
    