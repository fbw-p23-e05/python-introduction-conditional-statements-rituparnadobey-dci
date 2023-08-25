# Task 1 - calculate sum

num1 = int(input('Please enter 1st number: '))
num2 = int(input('Please enter 2nd number: '))
num3 = int(input('Please enter 3rd number: '))

if num1 == num2 == num3:
    sum_num = (num1 + num2 + num3) * 3
    print(sum_num,'is the total output')
else:
    sum_num = num1 + num2 + num3
    print('The total output is:',sum_num)


# task1 

num1 = int(input('First number: '))
num2 = int(input('Second number: '))
num3 = int(input('Third number: '))

if num1 == num2 == num3:
    sum_num = 3 * (num1 + num2 + num3)
else:
    sum_num = num1 + num2 + num3

print('The sum of numbers will be:',sum_num)

# task 2

num1 = int(input('First Number: '))
num2 = int(input('Second Number: '))


if num1 > num2:
    result = 2 * (num1 - num2)

else:
    result = abs(num1 - num2)

print('The calculation is:', result)


# Task 3

num = int(input('Number to check: '))


if num % 2 == 0:
    print(num,'is an even number')
else:
    print(num,'is an odd number')

# Task 4
import math

r = float(input('Input the Radius of the Circle: '))

area = math.pi * r**2

print('The  area of the circle with radius',r,'is:',area)



# Task 5


num = 7
guess = int(input('Guess a number between 1 and 10 until you get it right: '))

while guess != num:
    guess = int(input('Guess a number between 1 and 10 until you get it right: '))

print('Well Guessed!')


# Task 6

scale = ("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: ")

temperature = int(input("Input the value of temperature you'd like to convert: "))

if scale == 'C':
    result = (temperature / 5) + (32 / 9)
    print('The Temperature in Fahrenheit',result,'degrees')
elif scale == 'F':
    result = (temperature + (32 / 9)) *  5
    print('The Temperature in Celsius',result,'degrees')
else:
    print('Please insert in right format.')


# Task 7

print('*', 2 * '* ',3 * '* ',4 * '* ',sep='\n' )
for i in range (5, 0,-1):
    print(i * '* ')

# Task 8
num1 = 0
num2 = 1

while num1 <= 50:
    print(num1)
    # num1,num2 = num2,num1+num2
    num3 = num1 + num2
    num1 = num2
    num2 = num3