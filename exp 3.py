To receive two integers from key board and get their sum , product, subtraction through a user defined function:

def addition(x, y):

return (int(x+y))

def subtraction(x, y):

return (int(x-y))

def product(x, y):

return (int(x*y))

def division(x, y):

return (int(x/y))

x = int(input("Enter first integer "))

y = int(input("Enter second integer "))

print("Addition is: ", addition(x,y))

print("Subtraction is: ", subtraction(x,y))

print("Multiplication is: ", product(x,y))

print("Division is: ", division(x,y))







To define a function which computes the frequency of words present in a string passed to it

def count(string):

count_dict = {}

for ch in str(string):

if ch in count_dict:

count_dict[ch] += 1

else:

count_dict[ch] = 1

print(count_dict)

string = input ("Enter string ")

count(string)






To define a function to calculate the gross salary of an employee where gross salary is defined as basic salary+ DA+ HRA. DA is 80% of basic salary and HRA is 20% of basic salary. User input is basic salary.

def grossSalary(basic_salary):

DA = 0.8 * basic_salary

HRA = 0.2 * basic_salary

total_salary = basic_salary + DA + HRA

return total_salary

basic_salary = float(input("Enter your salary "))

print("Your total salary is ", grossSalary(basic_salary))







To define function to accept a group of numbers from keyboard and find their total and average

def sum(my_list):

sum = 0

for i in my_list:

sum += i

return sum

def avg(my_list):

return sum(my_list)/len(my_list)

my_list = []

number = int(input("How many numbers you want to enter: "))

for i in range(number):

my_list.append(int(input("Enter the number ")))

print("Sum of all enterd numbers is: ", sum(my_list))

print("Average of all enterd numbers is: ", avg(my_list))






