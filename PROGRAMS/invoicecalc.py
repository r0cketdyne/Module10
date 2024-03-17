#this prog will compute an invoice based on values entered by the user.
#the invoice computes a total (gross) bill amount based on the number of 
#hours invoiced and the hourly rate (the gross amount in the product of those two values)

#The user provides a discount code of 1, 2 or 3.

#1 is 10% discount
#2 is 12% discount
#3 is 15% discount

#any other value resuls in a discount of 0.

#all invoices must be printed to the screen

#after printing an invoice, ask user if they want to continue
#and enter another set of data (Y or N).
#you prog should loop as long as the response is a Y or a y

hourly_rate = float(input("Input the hourly rate: "))
hours_invoiced = float(input("Input the hours invoiced: "))
discount_code = int(input("Enter your discount code, if any: "))

gross_amount = hourly_rate*hours_invoiced

if discount_code == 1:
    # Computation for discount code 1
    discounted_amount = gross_amount * 0.9
    print("Discounted amount:", discounted_amount)
elif discount_code == 2:
    # Computation for discount code 2
    discounted_amount = gross_amount * 0.8
    print("Discounted amount:", discounted_amount)
elif discount_code == 3:
    # Computation for discount code 3
    discounted_amount = gross_amount * 0.7
    print("Discounted amount:", discounted_amount)
else:
    # Computation for no discount
    print("No discount applied.")