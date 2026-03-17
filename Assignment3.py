# Assignment Questions on Set (10)

# Q1. Create a set with numbers {1,2,3,4,5} and display it.
numbers = {1,2,3,4,5}
print(numbers)
print()

# Q2. Add an element 10 to a set {1,2,3}.
new = {1,2,3}
new.add(10)
print(new)
print()

# Q3. Remove the element 2 from the set {1,2,3,4} using .remove().
set1 = {1,2,3,4}
set1.remove(2)
print(set1)
print()

# Q4. Try to remove an element 100 from the set {1,2,3} using .discard() and check the difference with .remove().
set2 = {1,2,3}
#set2.remove(100)    #set2.remove(100) KeyError: 100
set2.discard(100)
print(set2)
print()

# Q5. Create two sets: A = {1,2,3,4} and B = {3,4,5,6}. Find:
# - Union
# - Intersection
# - Difference
A = {1,2,3,4} 
B = {3,4,5,6}
print("Union :",A|B)
print("Intersection",A&B)
print("Difference",A-B)
print()

# Q6. Check whether {1,2} is a subset of {1,2,3,4}.
A = {1,2}
B = {1,2,3,4}
print(A.issubset(B))
print()

# Q7. Check whether {1,2,3,4} is a superset of {1,2}.
A = {1,2,3,4}
B = {1,2}
print(A.issubset(B))
print()

# Q8. Create two sets {1,2} and {3,4} and check if they are disjoint.
A = {1,2}
B = {3,4}
print(A.isdisjoint(B))
print()

# Q9. Convert a list [1,2,2,3,4,4,5] into a set and display unique values.
list1 = [1,2,2,3,4,4,5]
s = set(list1)
print(s)
print()

# Q10. Find the length of a set {10,20,30,40,50}.
set1 = {10,20,30,40,50}
print(len(set1))
print()

# Assignment Questions on Dictionary (10)

# Q1. Create a dictionary with keys: name, age, city and assign some values. Print the dictionary.
new = {"name" : "chetna", "age" : 23, "city" : "pune"}
print(new)
print()

# Q2. Access the value of key "age" from dictionary {"name":"Akanksha", "age":25, "city":"Pune"}.
person = {"name":"Akanksha", "age":25, "city":"Pune"}
print(person["age"])
print()

# Q3. Add a new key-value pair "course":"Python" in the dictionary.
person = {"name":"Akanksha", "age":25, "city":"Pune"}
person["course"] = "Python"
print(person)
print()

# Q4. Update the value of "city" to "Mumbai" in dictionary {"name":"Rohan", "city":"Pune"}.
person = {"name":"Rohan", "city":"Pune"}
person["city"] ="Mumbai"
print(person)
print()

# Q5. Delete the key "age" from dictionary {"name":"Disha", "age":22, "city":"Nashik"}.
person = {"name":"Disha", "age":22, "city":"Nashik"}
person.pop("age")
print(person)
print()

# Q6. Write a program to get all the keys of dictionary {"a":1, "b":2, "c":3}.
person = {"a":1, "b":2, "c":3}
print(person.keys())
print()

# Q7. Write a program to get all the values of dictionary {"a":1, "b":2, "c":3}.
person = {"a":1, "b":2, "c":3}
print(person.values())
print()

# Q8. Merge two dictionaries: d1 = {"a":1, "b":2} and d2 = {"c":3, "d":4} using update method.
d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}
d3 = d1|d2
print(d3)
print()

# Q9. Write a program to access the value of "fees" from the above dictionary.

student = {
    "name": "Akanksha",
    "course": {
        "name": "Python",
        "duration": "3 months",
        "fees": 10000
    }
}
print(student["course"]["fees"])
print()

# Q10. Update the "department" of the employee from "IT" to "HR".

company = {
    "employee": {
        "id": 101,
        "name": "Rohan",
        "department": "IT"
    }
}

company["employee"] = "IT"
print(company)

