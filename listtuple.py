'''Basic Questions'''

'''1.Create a list of 5 cities and print the third city using positive indexing and the last city using negative indexing.'''
cities = ["nagpur","pune","mumbai","kolhapur","nashik"]
print("Third city:",cities[2])
print("last city:",cities[-1])

'''2.Write a program to create a list of first 10 odd numbers using manual entry.
'''
odd = [1,3,5,7,9,11,13,15,17,19]
print(odd)

'''3.Given a list nums = [2, 4, 6, 8, 10], access and print the second-last element using negative indexing.
'''
nums = [2,4,6,8,10]
print(nums[-2])

'''4.Concatenate the two lists a = [1,2,3] and b = [4,5,6] and print the result.
'''
a = [1,2,3] 
b = [4,5,6]
concatenate = a+b
print(concatenate)
'''5.Create a nested list and print a specific element (for example: from [1, [2,3,[4,5]], 6] print 5).
'''
li = [1, [2,3,[4,5]], 6]
print(li[1][2][1])

#Slicing & Indexing

'''1.Given colors = ["red","blue","green","yellow","black","white"],

	print ["green","yellow"] using positive slicing.

	print ["white","black"] using negative slicing.'''
colors = ["red","blue","green","yellow","black","white"]
print(colors[2:4])
print(colors[-1:-3:-1])

'''2.Create a list of first 15 even numbers and use slicing to display only numbers from 8 to 16.
'''
li = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
print(li[3:8])
'''3.Write a program to reverse a list using slicing.
'''
li = [1,2,3,4,5,6,7,8,9,10]
print(li[::-1])


'''4.From the list nums = [100,200,300,400,500,600], extract [300,400,500] using slicing.
'''
nums = [100,200,300,400,500,600]
print(nums[2:5])

'''5.Given x = [1,2,3,4,5,6,7,8,9], print only the odd numbers using step slicing.
'''
x = [1,2,3,4,5,6,7,8,9]
print(x[::2])
#Mutability & Modification

'''1.Create a list marks = [45, 56, 78, 89, 90]. Modify the second element to 60 and the last element to 95.
'''
marks = [45, 56, 78, 89, 90]
marks[1] = 60
marks[-1] = 95
print(marks)

'''2.Replace the middle three elements of [10,20,30,40,50] with [25,35,45].
'''
n = [10,20,30,40,50]
n[1:4] = [25,35,45]
print(n)

#List Methods

'''1.Create a list of names and add three new names using append().
'''
name = ["Radha","Shyam"]
name.append("Mohan")
print(name)


'''2.Create two lists of numbers and merge them using extend().
'''
a = [1,2,3,4]
b = [5,6,7,8]
a.extend(b)
print(a)

'''3.Insert "Python" at the 2nd position in the list ["Java","C++","C","Go"].
'''
list1 = ["Java","C++","C","Go"]
list1.insert(1,"Python")
print(list1)

'''4.Write a program to delete the element 500 from the list [100,200,300,400,500,600] using remove().
'''
lis = [100,200,300,400,500,600]
lis.remove(500)
print(lis)

'''5.Create a list [10,20,30,40,50], use pop() to delete the last element, and display the modified list.
'''
lis = [10,20,30,40,50]
lis.pop(-1)
print(lis)

'''6.Write a program to sort the list letters = ['d','a','z','c','b'] in ascending order and then in descending order.
'''
letters = ['d','a','z','c','b']
letters.sort
print("Ascending: ",letters)
letters.sort(reverse=True)
print("Desending: ",letters)

'''7.Create a list of numbers and display:

	Sum of all elements

	Maximum element

	Minimum element'''
numbers = [15,14,78,56,74,35,89]
print("Sum of all elaments: ",sum(numbers))
print("Maximum element: ",max(numbers))
print("Minimum elements: ",min(numbers))


#TUPLE QUESTIONS

'''1. Create a tuple with 5 integers and print its length.'''
tup = (1,2,3,4,5)
print(len(tup))

'''2. Create a tuple with 5 strings and print the second last element using negative indexing.'''
t = ("a","b","c","d","e")
print(t[-2])

'''3'. From the tuple (10,20,30,40,50), access elements from index 1 to 3 (inclusive of start, exclusive of end).'''
t = (10,20,30,40,50)
print(t[0:3])

'''4. Create a tuple ("a", "b", "c") and concatenate it with ("d", "e").'''
a = ("a", "b", "c")
b = ("d", "e")
concatenate = a+b
print(concatenate)

'''5. Create a tuple (100,). Print its type and explain why the comma is important.'''
t = (100,)
print(type(t)) # with comm is tuple (100,) ,without comms is int (100) ,

'''6. Create a tuple (1,2,3,4,5) and extract the last three elements using slicing.'''
tup = (1,2,3,4,5)
print(tup[2:])
print(tup[-3:])

'''7. Create a nested tuple (1, (2,3), (4,5,6)) and access 5.'''
n = (1, (2,3), (4,5,6))
print(n[2][1])

'''8. Swap two variables a=10 and b=20 using tuple unpacking.'''
a = 10
b = 20
a,b = b,a
print(a,b)

'''9. Create a tuple with duplicate values (5,5,5,10,20) and use count() to find how many times 5 appears.'''
d = (5,5,5,10,20)
c = d.count(5)
print(c)

'''10. Use the tuple (2,4,6,8,10) and check the index of element 8.'''
t = (2,4,6,8,10)
print(len(t))
print(t.index(8))

'''11. Demonstrate tuple packing: assign ("ram", 25, "pune") to a single variable.'''
person = ("ram", 25, "pune")
print(person)

'''12. Demonstrate tuple unpacking: from ("ram", 25, "pune") extract values into 3 different variables.'''
name,age,city = ("ram", 25, "pune")
print(name,age,city)

'''13. Create a tuple (1,2,3,4,5,6,7,8,9,10) and extract every second element using slicing.'''
t = (1,2,3,4,5,6,7,8,9,10)
print(t[1::2])

'''14. Create a tuple (1,2,3,4,5) and reverse it using slicing.'''
t = (1,2,3,4,5)
print(t[::-1])