#CTI 110
#P3HW2 Software Sales
# Daniel Kellberg
# June 22, 2018

def main():
    print('Hello World')



userNumberOfPackages = int(input( 'Please enter the number of packages bought '))
packagePrice = 99

if userNumberOfPackages < 10:
    discount = 0
elif userNumberOfPackages < 20:
    discount = .10
elif userNumberOfPackages < 50:
    discount = .30
elif unserNumberOfPackages < 100:
    discount = .40

subTotal = userNumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print()

print( 'Amount of discount: $' + format(discountAmount, ',.2f' )+ \
       '\nTotal amount: $' + format(total, ',.2f'))

main()

