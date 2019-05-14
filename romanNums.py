#user enters 1 integer in range from 1-10
#print Roman numeral version of that number if number is within range from 1-10
#let user know if number is out of range

try:
    RomanConvert = " "
    print('Enter an Integer in the range from 1 to 10')
    for num in range(1):
        digit = input('Enter an integer: ')
        digit = int(digit)
        if digit == 1:
            code = 'I'
        elif digit == 2:
            code = 'II'
        elif digit == 3:
            code = 'III'
        elif digit == 4:
            code = 'IV'
        elif digit == 5:
            code = 'V'
        elif digit == 6:
            code = 'VI'
        elif digit == 7:
            code = 'VII'
        elif digit == 8:
            code = 'IIX'
        elif digit == 9:
            code = 'IX'
        elif digit == 10:
            code = 'X'
        #code = '0'
    RomanConvert = RomanConvert + code
    print("The Roman Numeral conversion of that number is:", RomanConvert)
except:
    digit >10
    print('The number you entered is out of range')
    
