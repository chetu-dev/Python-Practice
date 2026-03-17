# TUPLE QUESTIONS

# 1. Create a tuple with 5 integers and print its length.
tup = (1,2,3,4,5)
print(tup)
print(len(tup))
print()

# 2. Create a tuple with 5 strings and print the second last element using negative indexing.
tup1 = ("a","b","c","d","e")
print(tup1[-2])
print()

# 3. From the tuple (10,20,30,40,50), access elements from index 1 to 3 (inclusive of start, exclusive of end).
tup2 = (10,20,30,40,50)
print(tup2[1:3])
print()

# 4. Create a tuple ("a", "b", "c") and concatenate it with ("d", "e").
tup3 = ("a", "b", "c")
tup_concate = tup3 + ("d","e")
print(tup_concate)
print()

# 5. Create a tuple (100,). Print its type and explain why the comma is important.
tup4 = (100,)       # with comma type is tuple and without comma type is int.
print(type(tup4))    #<class 'tuple'>
print()
#(100) - without comma type is int
#(100,) - with comma type is tuple

# 6. Create a tuple (1,2,3,4,5) and extract the last three elements using slicing.
tup5 = (1,2,3,4,5)
print(tup5[-3])
print()

# 7. Create a nested tuple (1, (2,3), (4,5,6)) and access 5.
t = (1, (2,3), (4,5,6))
print(t[2][1])
print()

# 8. Swap two variables a=10 and b=20 using tuple unpacking.
a=10  
b=20
a,b = b,a     #awapping usind tuple unppacking.
print("a =",a)
print("b =",b)
print()

# 9. Create a tuple with duplicate values (5,5,5,10,20) and use count() to find how many times 5 appears.
d = (5,5,5,10,20)
d_new = d.count(5)
print(d_new)
print()

# 10. Use the tuple (2,4,6,8,10) and check the index of element 8.
t1 = (2,4,6,8,10)
idx = t1.index(8)
print()

# 11. Demonstrate tuple packing: assign ("ram", 25, "pune") to a single variable.
person = ("ram", 25, "pune")
print(person)
print(type(person))
print()

# 12. Demonstrate tuple unpacking: from ("ram", 25, "pune") extract values into 3 different variables.
person = ("ram", 25, "pune")
name,age,city = person
print("name =",name)
print("age =",age)
print("city =",city)
print()

# 13. Create a tuple (1,2,3,4,5,6,7,8,9,10) and extract every second element using slicing.
new = (1,2,3,4,5,6,7,8,9,10)
print(new[1::2])
print()

# 14. Create a tuple (1,2,3,4,5) and reverse it using slicing.s
new1 = (1,2,3,4,5)
print(new1[::-1])
print()

# STRING QUESTIONS

# 15. Create a string "Python Programming" and print the first and last character.
string = "Python Programming"
print(string[0])
print(string[-1])
print()

# 16. From the string "HelloWorld", extract "Hello" using slicing.
string = "HelloWorld"
print(string[0:5])
print()

# 17. Concatenate two strings "Good" and "Morning" and print the result.
a = "Good"
b = "Morning"
new_concate = a + b
print("Concatenate two strings is :",new_concate)
print()

# 18. Convert the string "python" into uppercase and "PROGRAMMING" into lowercase.
print("python".upper())
print("PROGRAMMING".lower())
print()

# 19. Count how many times the letter "a" appears in "bananas".
print("bananas".count("a"))
print()

# 20. Find the index of the substring "World" in "Hello World".
print("Hello World".index("World"))
print()

# 21. Replace "Java" with "Python" in the string "I love Java".
print("I love Java".replace("Java","Python"))
print()

# 22. Remove extra spaces from the string " OpenAI ChatGPT " using a string method.
print(" OpenAI ChatGPT ".split())
print()

# 23. Take a string "hello world" and display the reverse of the substring "llo w" to "wo ll".
text = "hello world"
substring = text[2:7]
print(substring[::-1])
print()

# 24. Take the string "I\tlove\tPython". Replace the tab spaces \t with a single space " " and print the result.
print("I\tlove\tPython".replace("\t"," "))
print()

# 25. Take the string "red,green,blue,yellow". Split it and then join with " - " to get: "red - green - blue - yellow"
t = "red,green,blue,yellow"
result = " - ".join(t.split(","))
print(result)

# 26. Take the string "python java aws cloud". Convert it into a list of words, then join with "," to get: "python,java,aws,cloud"
t = "python java aws cloud"
words = t.split()
result = ",".join(words)
print(result)

# 27. Take the string "c,o,d,e,n,e,r,a". Convert it into "codenera" using a string method.
text = "c,o,d,e,n,e,r,a"
print(text.replace(",",""))
print()

# 28. Take the string "Learn@Python@With@Fun". Replace "@" with a space " " and print the final sentence.
text = "Learn@Python@With@Fun"
print(text.replace("@"," "))
print()

# 29. Take the string "banana". Use count() to find how many times "na" occurs.
text = "banana"
n_text = text.count("na")
print(n_text)
print()

# 30. Take the string "Python Programming". Find the index of the substring "gram".
print("Python Programming".index("gram"))
print()

# 31. Take the string "This is Python Python is easy". Replace only the first occurrence of "Python" with "Java".
text = "This is Python Python is easy"
print(text.replace("Python","Java",1))
print()

# 32. Take the string "openAI,chatGPT,python". Split it into a list, then join using " | " to get: "openAI | chatGPT | python"
text = "openAI,chatGPT,python"
result = " | ".join(text.split(","))
print(result)
print()

# 33. Take the string "Mississippi". Use count() to find how many times "ss" appears.
text = "Mississippi"
print(text.count("ss"))
print()
