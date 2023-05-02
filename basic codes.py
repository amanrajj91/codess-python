To find area, circumference and volume of the sphere

import numpy as np

print("SPHERE: area, circ, vol")

rad=float(input("Enter the radius: "))

arS=(4*np.pi*rad**2)

print("The area is: ", arS)

circ=(2*np.pi*rad)

print("The circumference is: ", circ)

volS=4/3*np.pi*rad**3

print("The volume is: ", volS)

print("----------------------------------")






To find area, perimeter, and volume of the Cube.

print("CUBE: area, circ, vol")

side=float(input("Enter the side: "))

arC=(6*side**2)

print("The area is: ", arC)

perimeter=12 * side

print("The perimeter is: ", perimeter)

volC=side**3

print("The volume is: ", volC)

print("----------------------------------")







To print all even numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:

if num % 2 == 0:

print(num)






To print all positive numbers in a list

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]

for num in numbers:

if num > 0:

print(num)






To find maximum of three numbers

print("To find maximum of three numbers")

a = float(input("Enter first number: "))

b = float(input("Enter second number: "))

c = float(input("Enter third number: "))

if(a > b and a > c):

print("a is greater")

elif(b > a and b > c):

print("b is greater")

else:

print("c is greater")







To find the roots of the given quadratic equation

import numpy as np

import cmath

print("To find quadratic equation")

a = int(input("Enter coefficient of A: "))

b = int(input("Enter coefficient of B: "))

c = int(input("Enter coefficient of C: "))

d = cmath.sqrt((b**2) - 4*a*c)

r1 = (-b + d)/2*a

r2 = (-b - d)/2*a

print('The solution are {0} and {1}'.format(r1,r2))









To find whether the entered character is vowel or consonant

print("CHARACTER IDENTIFICATION")

ch = input("Enter the character : ")

if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):

print("Vowel")

if (ch.isdigit() == True):

print("Number")

else:

print("Consonants")









To find factorial of the given number entered through keyboard

number = int(input("Enter the number whose factorial is to be calculate "))

factorial = 1

while(number > 0):

factorial *= number

number -= 1

print(factorial)









To find reverse of 5-digit number using while loop

number = int(input("Enter 5 digit number "))

rev_number = 0

while number > 0:

rev_number += number%10

number = int(number/10)

if number == 0:

break

rev_number *= 10

print(rev_number)






To count the number of alphabets and digits in a keyboard using while loop

str_inp = input("Enter a string ")

count_alphabets = 0

count_digits = 0

for ch in str_inp:

if ch.isdigit():

count_digits += 1

if ch.isalpha():

count_alphabets += 1

print("Count of alphabets ", count_alphabets)

print("Count of digits ", count_digits)









To determine the youngest of three if their ages are entered through keyboard

age1 = int(input("Enter age of person 1: "))

age2 = int(input("Enter age of person 2: "))

age3 = int(input("Enter age of person 3: "))

youngest = age1

if age2 < youngest:

youngest = age2

if age3 < youngest:

youngest = age3

print("The youngest person's age is:", youngest)






To generate the given patterns

rows = int(input("Enter number of rows"))

for i in range(1, rows+1):

for j in range(1, i+1):

print("*", end='')

print('')




ows = int(input("Enter number of rows "))

for i in range(1, rows+1):

for j in range(1, i+1):

print("*", end='')

print('')

for i in range(rows+1, 1, -1):

for j in range(0, i-1):

print("*", end='')

print('')







row = int(input("Enter number of rows "))

for i in range(row):

for j in range(row - i - 1):

print(' ', end='')

for k in range(2 * i + 1):

print(k + 1, end='')

print()










