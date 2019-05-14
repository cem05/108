#This program will ask for amount of borrowed, amount of interest
#, and the number of months of the loan to calculate the payement

print('We are going to calculate the monthly payment of a loan...\n')
borrowed = input('What is the amount borrowed on the loan? ')
borrowed = float(borrowed)
interest = input('What is the interest rate on the loan? Enter the percentage: ')
interest = float(interest)
interest = interest/100
months = input('How long is the loan? Enter the # of months: ')
months = int(months)

#calculate monthly payment
payment = (borrowed*(interest/12)*(1+interest/12)**months)/(((1+interest/12)**months)-1)
payment = format(payment, '.2f')

#print the results
print('\n')
print('The amount of the loan is: $', str(borrowed))
print('The interest rate is: ', str(interest) + '%')
print('The length of the loan is: ', str(months) + ' months')
print('The monthly payement is: $', str(payment))
print('\n')
      

