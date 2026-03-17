# Part 1: Coding Questions (40) 

# Classes and Objects: 
# 1. Create a class Person with attributes name and age. 
class Person:
    name = "Chetna"
    age = 24
p1 = Person()
print("Name :",p1.name)
print("Age :",p1.age)
print()

# 2. Create two objects of the Person class and print their details. 
class Person1:
    pass
obj1 = Person1()
obj1.name = "Abhi"
obj1.age = 24

obj2 = Person1
obj2.name = "Chetu"
obj2.age = 24

print("obj1:",obj1.name,obj1.age)
print("obj2:",obj2.name,obj2.age)


# 3. Add a method display() to print the object details. 
# 4. Update the age of a person object. 
# 5. Delete an attribute of a person object. 


# Constructor & Self: 
# 6. Create a class Student with a constructor to initialize name and marks. 
# 7. Print student details using self. 
# 8. Create multiple student objects and print their marks. 
# 9. Add default values to the constructor parameters. 
# 10. Use __del__ method to print a message when an object is deleted.