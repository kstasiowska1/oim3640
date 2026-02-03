#Practical use of modulo operator to check if a number is odd or even
a = input("Enter an integer: ")
a = int(a)
print(type(a))

#check odd or even
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

a = 2
1 + a #an expression, which evaluates to 3, but does not do anyhting with it
print (1 + a) #a statement which prints the results (3)

#a product would cost $100, how much tax do we pay?
product = 100 #in dollars
tax_rate = 0.0625
tax = product * tax_rate
print(f'Tax is for the products which costs ${product} is ${tax}')

#doing the same thing with a function
computer_price = 900
iphone_price = 1100

def calc_tax(price, tax_rate):
    """Calculate product tax based on given price."""
    tax_rate = 0.0625
    tax = price * tax_rate
    #print(f'Tax is for the products which costs ${price} is ${tax}')
    #print(tax)
    #if the function does not explicitly return any value, it would return None
    return tax

computer_price = float(input('Enter the product price:  '))
iphone_price = 1100
mass_rate = 0.0625
ny_rate = 0.0875

tax_computer = calc_tax(computer_price, mass_rate)
tax_iphone =calc_tax(iphone_price, ny_rate)

total_tax = tax_computer + tax_iphone
print(total_tax)