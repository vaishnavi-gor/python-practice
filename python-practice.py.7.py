print("Please enter your memnbership type: Gold/Silver/None")
membership_type = input()
print("Please enter your purchase amount")
purchase_amount = int(input())
if membership_type == "Gold" and purchase_amount >= 500:
    discount = purchase_amount * 0.20
    final_price = purchase_amount - discount
    print("20% discount!")
    print("Final price is:",final_price)
elif membership_type == "Silver" and purchase_amount >= 500:
    discount = purchase_amount * 0.10
    final_price = purchase_amount - discount
    print("10% discount!")
    print("Final price is:", final_price)
else:
     print("No discount!") 
     print("Final price is:", purchase_amount)
     


      
     
     