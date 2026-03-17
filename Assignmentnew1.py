# Part 1: Coding Questions (10) 

# 1. Declare variables of different types 
#  Task: Declare a string, int, float, and boolean variable. 
name = "chetna"
age = 23
aprice = 200.2
is_student = True
print(name)
print(age)
print(aprice)
print(is_student)
print()

# 2. Type Casting: Int to Float 
#  Task: Convert an integer variable to float and print its type. 
age = 23
newage = float(age)

print(newage)
print(type(newage))
print()

# 3. Type Casting: String to Int 
#  Task: Take a string containing a number and convert it to integer. 
num = "45"
newnum = int(num)
print(newnum)
print(type(newnum))
print()

# 4. Swap two variables without using a third variable 
#  Example: a = 5, b = 10 → swap values. 
a = 5
b = 10
a,b = b,a
print("Swap a,b :",a,b) 
print()

# 5. Swap two variables using a temporary variable 
#  Task: Use a temporary variable to swap two numbers. 
a = 5
b = 10
temp = a
a = b
b = temp
print(a,b)
print()

# 6. Sum of two numbers with type casting 
#  Task: Take one input as string, one as int → convert appropriately → sum them. 
num1 = "45"
num2 = 78
num3 = int(num1) + num2
print(num3)
print()

# 7. Concatenate two variables of different types 
#  Example: a = "Hello", b = 5 → make output: "Hello5".
a = "chetna"
b = 23
c = a + str(b)
print(c)
print()

# 8. Check type of input variable 
#  Task: Input a value and print its type before and after type casting. 
val = "25"
print(val)
print(type(val))
val = int(val)
print(type(val))
print()

# 9. Convert float to int and vice versa 
#  Task: Convert a float to int and an int to float. 
num_float = 45.4
num_int = int(num_float)
print(num_int)

num2 = 10
num2_float = int(num2)
print(num2_float)
print()

# 10. Multiple assignment and swapping 
#  Task: Assign a=1, b=2, c=3 in a single line and swap a and c in one line.
a=1
b=2
c=3 

a,c = c,a
print(a,b,c)
print()

'''Part 2: Interview Questions (10) 

1. What is a variable in Python? 
A variable is container used to store data in memory location
x = 10
hear x is variable nad 10 is value store in memory location

2. Explain the difference between mutable and immutable types. 
Mutable Data Types :
Can be modified after creation.
Examples:
list, dict, set
Example:
my_list = [1, 2, 3]
my_list.append(4)
List changes in same memory location.

Immutable Data Types :
Cannot be changed after creation.
Examples:
int, float, str, tuple, bool
Example:
a = 10
a = 20
Here new object is created. Old object remains unchanged.

3. What is type casting in Python? 
Type casting means converting one data type to another.
int("5")
float(10)
str(20)

4. Difference between int(), float(), str() type casting? 
int() → converts to integer
float() → converts to decimal number
str() → converts to string

5. How do you swap two variables in Python without a third variable? 
a, b = b, a

6. Can you change the type of a variable after declaring it? Explain. 
yes 
Because Python is:
 Dyamically Typed Language
x = 10
x = "Hello"
x = 3.5
Type is determined at runtime.
Important?
Flexible coding
Faster development
Less boilerplate code

7. What happens if you try to add a string and an integer in Python? 
"5" + 5
TypeError
Because Python is strongly typed language.
It does NOT automatically convert string to int.
Correct Way:
int("5") + 5

8. What is the difference between = and == in Python? 
= (Assignment Operator)
Stores value in variable.
x = 5
== (Comparison Operator)
Checks equality of values.
x == 5
Returns True/False.


9. Explain multiple assignment in Python with an example. 
Assign multiple variables in one line.
a, b, c = 1, 2, 3
Also Used For:
Swap
a, b = b, a
Same value
x = y = z = 0
def get_user():
    return "Chetna", 22

name, age = get_user()


10. What is the difference between is and ==?
Checks if values are equal.

a = [1,2]
b = [1,2]
a == b     #True

'''

# Part 3: Guess the Output (5) 
# Q1: 
# a = 5 
# b = 2 
# a, b = b, a 
# print(a, b)  
#output = 2 5

# Q2: 
# x = "5" 
# y = 3 
# print(int(x) + y) 
#output = 8

# Q3: 
# a = 3.7 
# print(int(a)) 
#output = 3

# Q4: 
# a = 10 
# b = 20 
# a = a + b 
# b = a - b 
# a = a - b 
# print(a, b) 
#output = 20 10

# Q5: 
# x = "Python" 
# y = 3 
# print(x * y)
#output = PythonPythonPython