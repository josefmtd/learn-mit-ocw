balance = float(input('Enter the outstanding balance on your credit card:'))
interest = float(input('Enter the annual credit interest rate as a decimal:'))

for paid_minimum in range(10,int(balance),10):
    balance_now = balance
    for month in range(1,13):
        paid_interest = interest/12 * balance_now
        paid_principal = paid_minimum - paid_interest
        balance_now = balance_now - paid_principal
        if balance_now < 0:
            break
    if balance_now < 0:
        break

print('Monthly payment to pay off debt in 1 year:', str(paid_minimum))
print('Number of months needed:', str(month))
print('Balance:', str(round(balance_now,2)))
