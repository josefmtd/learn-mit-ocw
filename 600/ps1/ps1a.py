balance = float(input('Enter the outstanding balance on your credit card:'))
interest = float(input('Enter the annual credit interest rate as a decimal:'))
minimum = float(input('Enter the minimum monthly payment rate as a decimal:'))

for month in range(1,13):
    print('Month:',str(month))
    paid_minimum = minimum * balance
    paid_interest = interest/12 * balance
    paid_principal = paid_minimum - paid_interest
    balance = balance - paid_principal
    print('Minimum monthly payment: $' + str(round(paid_minimum,2)))
    print('Principle paid: $' + str(round(paid_principal,2)))
    print('Remaining balance: $' + str(round(balance,2)))
