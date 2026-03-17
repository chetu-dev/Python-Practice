#1.Take your name as input and print:
#o/p - Hello, <name>! Welcome to Python.

name = input("Enter your name :")
print("Hello,", name + "! Welcome to python")

'''2.Take your age as input and print:
o/p - You are <age> years old. Next year, you will be <age+1>.
'''
age = int(input("Enter your age : "))
print("you are,", age, " years old.", "Next year, you will be", age + 1 )

'''
3.Take length and width as input and print:
o/p - The area of rectangle with length <length> and width <width> is <area>.
'''
length = float(input("Enter a length :"))
width = float(input("Enter a width :"))
print(length)
print(width)
area = length * width
print("The area of rectangle with length", length , "and width", width, "is", area)

'''
4.Take radius as input and print:
o/p - The circumference of a circle with radius <r> is <2 * 3.14 * r>.
'''
r = float(input("Enter a radius :"))
print(r)
circumference = 2 * 3.14 * r
print("The circumferance of circle with radius", r, "is", circumference )

'''5.Take first name and last name as input and print:
	o/p - Your full name is <firstname lastname>.
'''
f_name = input("Enter a first name :")
l_name = input("Enter a last name :")
print("your full name is",f_name,l_name)

'''6.Take principal, rate, and time as input and print:
	o/p - Simple Interest for principal <P>, rate <R>% and time <T> years is <SI>.
'''
P = float(input("Enter principal :"))
R = float(input("Enter rate :"))
T = float(input("Enter time :"))
SI = (P*R*T) / 100
print(f"simple Interest for principal {P}, rate {R}%, time {T} years is {SI}.")

'''output 
Enter principal :10000
Enter rate :5
Enter time :2
simple Interest for principal 10000.0, rate 5.0%, time 2.0 years is 1000.0.'''

'''
7.Take Celsius as input and print:
	o/p - <C>°C is equal to <F>°F.
(Formula: F = (C*9/5) + 32)'''
C = float(input("Enter a celsius :"))
F = (C*9/5) + 32
print(f"{C}°C is equal to {F}°F.")

# output =Enter a celsius :5
# 5.0°C is equal to 41.0°F.

'''
8.Take marks in 5 subjects as input and print:
	o/p - You scored <percentage>% in total.'''

marks1 = float(input("Enter marks1 :"))
marks2 = float(input("Enter marks2 :"))
marks3 = float(input("Enter marks3 :"))
marks4 = float(input("Enter marks4 :"))
marks5 = float(input("Enter marks5 :"))
total = marks1+marks2+marks3+marks4+marks5
percentage = total/5
print(f"you score {percentage}% in total.")

# output = Enter marks1 :89
# Enter marks2 :78
# Enter marks3 :85
# Enter marks4 :96
# Enter marks5 :32
# you score 76.0% in total.
'''
9.Take item name, quantity, and price per unit as input and print:
	o/p - The total cost for <quantity> <itemname>(s) at Rs.<price> each is Rs.<total>.'''
item = input("Enter item name : ")
quantity = int(input("Enter quantity : "))
price = float(input("Enter price : "))
total = quantity * price
print(f"The total cost for {quantity} {item}s at Rs.{price} each is Rs{total}.")

# output =Enter item name : book
# Enter quantity : 56
# Enter price : 90
# The total cost for 56 books at Rs.90.0 each id Rs5040.0.
'''
10.Take a number as input and print:
	o/p - The square of <n> is <n**2> and the cube is <n**3>.'''
n = int(input("Enter a number : "))
print(f"The squre of {n} is {n**2} and the cube is {n**3}.")
# output = Enter a number : 5
# The squre of 5 is 25 and the cube is 125.

'''
11.Take a number as a string input and convert it into an integer. Print its square.'''
s = input("Enter a number :")
s = int(s)
print(s**2)
# output = Enter a number :45
# 2025

'''12.Take an integer input and convert it to float. Print both values.'''
num = int(input("Enter a number:"))
f = float(num)
print(num,f)
# output = Enter a number:45
# 45 45.0

'''13.Take a decimal number input and convert it into an integer. Print both values.'''

num = float(input("Enter a integer:"))
d = int(num)
print(num,d)

# output = Enter a integer:45.12
# 45.12 45

'''14.Take a number as input and convert it into a string. Print "The number is <num>" using f-string.'''
num = int(input("Enter  number :"))
new = str(num)
print(f"The number is {new}")
print(type(new))

#  output = Enter  number :465656
# The number is 465656
# <class 'str'>

'''15.Take two numbers as string input. Convert them into integers and print their sum.'''
num1 = input("Enter a number:")
num2 = input("Enter a number:")
print(int(num1) + int(num2))

# output Enter a number:78
# Enter a number:96
# 174

'''16. Create a variable name with your name and print:
My name is <name>'''
name = "chetna"
print(f"My name is {name}")


'''17. Store your age in a variable and print:
I am <age> years old.'''
age = 23
print(f"I am {age} years old.")

'''18. Store two numbers in variables a and b. Print their sum.'''
a = 45
b =78
sum = a + b
print(sum)

'''19. Store the value of π = 3.14159 in a variable and print:
Value of π is 3.14159'''
pi = 3.14159
print(f"Value of π is {pi}")

'''20. Create a variable country with your country name and print:
I live in <country>'''
country = "India"
print(f"I live in {country}")

'''21. Store two strings in variables and print them together as a sentence.'''
a = "What is your name"
b = "chetna sarode"
print(a + " " + b)
print()

'''22. Store marks of 3 subjects in variables and print the total.'''
m1 = 89
m2 = 90
m3 = 78
print(m1 + m2 +m3)
print()

'''23. Assign True to a variable and print its type using type().'''
num = True
print(type(num))

'''24. Store a float number in a variable and print:
The number is <value>'''
num = 1254.45
print(f"The number is {num}.")

