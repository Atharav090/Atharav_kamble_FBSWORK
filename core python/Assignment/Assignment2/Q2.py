# WAP to Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
#  take input
C = float(input("Enter the temprature in Celcius: "))
#  convert Celcius to Fahrenheit
F = 9 * (C / 5 ) + 32
#  Display results
print(f'The temprature {C} C in Fahrenheit is: {F} F')