# # Variables in Python
# studentname = "Muhammad Salman"
# print(studentname)
#
# classname = "BS Computer Science"
# print(classname)
#
# subjectname = "Android Application Development"
# print(subjectname)
# # Data Types
# # Check Data Type
# print(type(subjectname))
# # Operators in Python
# a = 10
# b = 50
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
#
# # Rational
# a = 50
# b = 20
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
#
# # Find Word with help of Index
# strr = "Muhammad Salman"
# print(strr [11])
# # Length Of String
# strr = "Muhammad Salman"
# print(len(strr))
# # String Lower and Upper Case
# print(strr.lower())
# print(strr.upper())
# # String Count
# strr = "This String is a String"
# print(strr.count("String"))
# # String Find
# print(strr.find("String"))
# # Split String
# city = ("I Like FSD, Lahore, ISB, Peshawar and Balochistan")
# print(city.split("ISB"))

# Tuples
# tup = (1, 'a', True, 555.4)
# print(tup)
# # Extracting Individual Elements
# print(tup[3])
# print(tup[0:1])
# # Length of Tuple
# print(len(tup))
# # Concatenation of Tuple
# tup1 = (1,2,3)
# tup2 = (4,5,6)
# # print(tup1+ tup2)
# # print(tup2 + tup1)
# # Repeating Tuple Elements
# tup1*3
# # Repeating and concatenation
# print(tup2*2+tup1)
# # Minimum & Maximum Value
# print(min(tup1))
# print(max(tup2))

# l = [1, 22.22, 'salman', False]
# print(l)
# print(l [0:3])
# Appending a new Element
# print(l.append(5))
# print(l)
# # Poping of last element
# l.pop()
# print(l)
# # Sorting List Element
# l = [1,4,5,7,8,9,2,3,10,45]
# l.sort()
# print(l)
# # Reversing of Elements
# l = [4,5,2,1,3,7,8,9]
# # l.reverse()
# # print(l)
# # Inserting of Element
# l.insert(1, "M. Salman")
# print(l)
# # Concatenation of Elements
# l = [1,2,3,4]
# l1 = [6555]
# print(l+l1)
# # Repeating of Elements
# print(l1*2)
#
# # Dictionary In Python
# d = {"apple": 20, "orange":50}
# # Extracting Keys
# print(d.keys())
# # Extracting Values
# print(d.values())
#
# # Update one dictionary elements with others
# d1 = {"apple": 20, "orange": 30, "banana":50}
# d2 = {"fsd": 5000}
# d1.update(d2)
# print(d1)
#
# d1.pop("apple")
# print(d1)

# Set of Elements
# s1 = {1, 'a', 3.145}
# print(s1)
# # Adding
# s1.add("M. Salman")
# print(s1)
# # Multiple Elements
# s1 = {12, 'k', 20.3}
# s1.update([566,78,20])
# print(s1)
# # Remove
# s1.remove(566)
# print(s1)
# # Union of Two Sets
# a = {5,6,7}
# b = {'a','v','g', 1,2,5}
# print(a.union(b))
# # Intersection
# print(a.intersection(b))

# Create Class
class MyClass ():
    x = 10
# Create Object
x1 = MyClass ()
print(x1.x)

# init Function
class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Salman", 22)

print(p1.name)
print(p1.age)





