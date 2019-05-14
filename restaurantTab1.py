#this program will calculate a restauraunt tab with a gift certificate

#cost of certificate
certificate = float(input('enter amount of gift certificate: '))

#cost of ordered items
print('\nenter ordered items for person 1')
appetizerPer1 = float(input('Appetizer: '))
entreePer1 = float(input('Entree: '))
drinksPer1 = float(input('Drinks: '))
dessertPer1 = float(input('Dessert: '))

print('\nenter ordered items for person 2')
appetizerPer2 = float(input('Appetizer: '))
entreePer2 = float(input('Entree: '))
drinksPer2 = float(input('Drinks: '))
dessertPer2 = float(input('Dessert: '))

#total items
amtPerson1 = appetizerPer1 + entreePer1 + drinksPer1 + dessertPer1
amtPerson2 = appetizerPer2 + entreePer2 + drinksPer2 + dessertPer2

#sales tax entered by user
tax = float(input('\nUser enters the tax rate percentage: '))

#compute tab including tax
itemsCost = amtPerson1 + amtPerson2
tab = itemsCost + (itemsCost * tax)

#format for total of 5 characters (including decimal point and decimals & 2 floating)
print('Ordered Items: ${0:5.2f}'.format(itemsCost))
print('Restaurant Tax: ${0:5.2f}'.format(itemsCost * tax))
print('tab: ${0:5.2f}'.format(tab - certificate))
print('(negative amount indicates unsused amount of gift certificate)')
