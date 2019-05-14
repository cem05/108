#unique conversion problem, something different
#Currency Conversion to Euros from US Dollars
#1 EURO (EUR) = 1.2043 U.S. dollar (USD)
#from https://www.wellsfargo.com/foreign-exchange/currency-rates/ on 10/23/2018

print('This program can be used to convert to Euros from US Dollars.')
print('The exchage rate was taken from https://www.wellsfargo.com/foreign-exchange/currency-rates/ on 10/03/2018, and was 1 EURO (EUR) = 1.2187 U.S. dollar (USD)')
Euro = 1
USD = 1.2043

print('\n')
usd_exchanged = input('Enter amount of whole dollars to be converted: ')
usd_exchanged = int(usd_exchanged)
euro_received = usd_exchanged//USD

print('You receive',int(round(euro_received)),'Euros, rounded down to the nearest Euro, as we only convert to whole Euros.')

#conversion fee from WellsFargo is 7$ flat fee if converting under 1000 USD
#and free at or above 1000 USD and over free
print('The conversion fee from WellsFargo is 7$ flat fee if converting under 1000 USD and free at or above 1000 USD')

if usd_exchanged >= 1000: print('You owe Wells Fargo',(usd_exchanged),'dollars.')
if usd_exchanged < 1000: print('You owe Wells Fargo',(usd_exchanged + 7),'dollars.')
