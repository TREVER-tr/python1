#Python has several basic operations that are essential for programming. Here are some key ones with example codes:
# 1 Arithmetic Operations
a = 10
b = 3

print("Addition:", a + b)       # 10 + 3 = 13
print("Subtraction:", a - b)    # 10 - 3 = 7
print("Multiplication:", a * b) # 10 * 3 = 30
print("Division:", a / b)       # 10 / 3 = 3.33
print("Floor Division:", a // b) # 10 // 3 = 3
print("Modulo:", a % b)         # 10 % 3 = 1
print("Exponentiation:", a ** b) # 10^3 = 1000

# 2 Comparison Operators
x = 5
y = 10

print("Equal:", x == y)        # False
print("Not Equal:", x != y)    # True
print("Greater Than:", x > y)  # False
print("Less Than:", x < y)     # True
print("Greater or Equal:", x >= y) # False
print("Less or Equal:", x <= y) # True


# 3 Logical Operators
a = True
b = False

print("AND:", a and b)  # False
print("OR:", a or b)    # True
print("NOT:", not a)    # False


 # 4 Bitwise Operators
x = 5  # 0101 in binary
y = 3  # 0011 in binary

print("Bitwise AND:", x & y)  # 0101 & 0011 = 0001 (1)
print("Bitwise OR:", x | y)   # 0101 | 0011 = 0111 (7)
print("Bitwise XOR:", x ^ y)  # 0101 ^ 0011 = 0110 (6)
print("Bitwise NOT:", ~x)     # -(x+1) = -6
print("Left Shift:", x << 1)  # 0101 << 1 = 1010 (10)
print("Right Shift:", x >> 1) # 0101 >> 1 = 0010 (2)

# 5  Assignment Operators
x = 10
x += 5  # x = x + 5
print("Addition Assignment:", x)  # 15

x -= 3  # x = x - 3
print("Subtraction Assignment:", x)  # 12

x *= 2  # x = x * 2
print("Multiplication Assignment:", x)  # 24

x /= 4  # x = x / 4
print("Division Assignment:", x)  # 6.0

 # 6️ Membership Operators
text = "Hello Python"
print("Is 'Python' in text?", "Python" in text)  # True
print("Is 'Java' not in text?", "Java" not in text)  # True


 # 7 Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)  # True (same object)
print("a is c:", a is c)  # False (different objects with same values)
print("a is not c:", a is not c)  # True

# Comparison Operators
print(5 > 3)  # True

# 8 Strings Operations
text = "Hello, Python!"

print("Uppercase:", text.upper())  # Convert to uppercase
print("Lowercase:", text.lower())  # Convert to lowercase
print("Title Case:", text.title())  # Capitalize each word
print("Replace:", text.replace("Python", "World"))  # Replace substring
print("Split:", text.split())  # Split into a list by spaces
print("Join:", "-".join(["Hello", "Python"]))  # Join list items into a string
print("Find 'Python':", text.find("Python"))  # Find index of substring
print("Length:", len(text))  # Get length of the string

 # 9 List Operations
fruits = ["apple", "banana", "cherry"]

print("Original List:", fruits)
fruits.append("orange")  # Add item
print("After Append:", fruits)

fruits.remove("banana")  # Remove item
print("After Remove:", fruits)

print("Sorted List:", sorted(fruits))  # Sort list
print("Reversed List:", fruits[::-1])  # Reverse list
print("Index of 'cherry':", fruits.index("cherry"))  # Get index of item

 # 10 Tuple Operations
numbers = (1, 2, 3, 4, 5)

print("Original Tuple:", numbers)
print("Length of Tuple:", len(numbers))  # Get length
print("Access First Element:", numbers[0])  # Access element
print("Slicing Tuple:", numbers[1:4])  # Slice a portion




# 11 Dictionary Operations
person = {"name": "Alice", "age": 25, "city": "New York"}

print("Original Dictionary:", person)
print("Access Name:", person["name"])  # Access value by key
person["age"] = 26  # Update value
print("Updated Age:", person["age"])

print("Keys:", person.keys())  # Get all keys
print("Values:", person.values())  # Get all values
print("Items:", person.items())  # Get key-value pairs

person.pop("city")  # Remove key-value pair
print("After Removing City:", person)

# 12  Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)  # Combine both sets
print("Intersection:", set1 & set2)  # Common elements
print("Difference:", set1 - set2)  # Elements in set1 not in set2
print("Symmetric Difference:", set1 ^ set2)  # Elements in either set but not both


 #13  Loops (For & While)
# For Loop
for i in range(5):  
    print("For Loop Iteration:", i)

# While Loop
count = 0
while count < 5:
    print("While Loop Count:", count)
    count += 1



# 14 Functions in Python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Call function with argumen
#15 Functions with Arguments & Return Values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)  # Output: 8


# Functions can take parameters and return values.

# 16 Lambda Functions (Anonymous Functions)
square = lambda x: x ** 2
print("Square of 4:", square(4))  # Output: 16


# Lambda functions are short, one-line functions without a name.

# 17 List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print("Squared List:", squared)  # Output: [1, 4, 9, 16, 25]


# List comprehensions provide a concise way to create lists.

#18 Exception Handling
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("Invalid input! Please enter a number.")


# try-except blocks handle errors gracefully.

#19 File Handling
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:", content)


# open() is used to read and write files.

# 20 Object-Oriented Programming (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p1 = Person("Alice", 25)
print(p1.greet())  # Output: Hello, my name is Alice and I am 25 years old.

# Classes & Objects allow structured programming.

 # 21 Inheritance in OOP
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())  # Output: Woof!


# Inheritance allows a class to inherit properties from another class.

# 22 Modules & Importing
import math

print("Square root of 16:", math.sqrt(16))  # Output: 4.0


 # Modules provide reusable functions.

# 23Regular Expressions (Regex)
import re

pattern = r"\d+"  # Matches numbers
text = "My age is 25"

match = re.findall(pattern, text)
print("Matched Numbers:", match)  # Output: ['25']


#Regex helps in pattern matching.

# 24 Multithreading
import threading

def print_numbers():
    for i in range(5):
        print(i)

t1 = threading.Thread(target=print_numbers)
t1.start()


#  Multithreading allows parallel execution.
