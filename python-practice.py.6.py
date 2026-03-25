print("Please enter your memnbership type: Gold/Silver/None")
membership_type = input()
print("Please enter your purchase amount")
purchase_amount = int(input())
if membership_type == "Gold" and purchase_amount >= 500:
    print("20% discount!")
elif membership_type == "Silver" and purchase_amount >= 500:
     print("10% discount!")
else:
     print("No discount!")    
     


      
     
     