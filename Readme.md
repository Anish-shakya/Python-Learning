📘 Welcome to My Python Learning Journey! 🚀

Hello there! 👋 I’m Anish, and I’m on an exciting journey to become a Data Analyst using Python! 🐍📊

This repository is my personal learning tracker, where I document everything I learn about Python, data analysis, and related technologies. Whether it’s coding basics, data manipulation, visualization, I’ll be sharing my progress here.

# Python Basics

This document covers the foundational concepts of Python programming with simple examples and explanations.

## 1. Variables

Variables are used to store data. You don't need to declare the data type explicitly.

python
name = "Alice"
age = 25
pi = 3.14


2. Data Types

Python supports several built-in data types:
	•	int: Integer numbers
	•	float: Decimal numbers
	•	str: String (text)
	•	bool: Boolean (True/False)
	•	list, tuple, dict, set: Collection types

a = 10            # int
b = 5.5           # float
c = "Hello"       # str
d = True          # bool



⸻

3. String and Its Functions

Strings are sequences of characters.

text = "Hello, Python!"

# Common string functions
print(text.upper())        # HELLO, PYTHON!
print(text.lower())        # hello, python!
print(text.capitalize())   # Hello, python!
print(text.replace("Python", "World"))  # Hello, World!
print(len(text))           # 14
print(text[0:5])           # Hello



⸻

4. List and Its Functions

Lists are ordered, mutable collections.

fruits = ["apple", "banana", "cherry"]

# Common list functions
fruits.append("orange")
fruits.remove("banana")
print(fruits[0])          # apple
print(len(fruits))        # 3
fruits.sort()
print(fruits)



⸻

5. Tuples

Tuples are ordered, immutable collections.

coordinates = (10, 20)

# Accessing tuple elements
print(coordinates[0])     # 10



⸻

6. Dictionary

Dictionaries store key-value pairs.

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])        # Alice

# Adding/updating
person["email"] = "alice@example.com"

# Looping through dictionary
for key, value in person.items():
    print(key, ":", value)



⸻

7. Set

Sets are unordered collections of unique items.

numbers = {1, 2, 3, 3, 4}

# Set operations
numbers.add(5)
numbers.remove(3)
print(numbers)



⸻

8. Loops and Its Types

a) for Loop

Used for iterating over a sequence.

for i in range(5):
    print(i)

b) while Loop

Repeats as long as a condition is true.

count = 0
while count < 5:
    print(count)
    count += 1



⸻

End of Notes

---

Let me know if you'd like to include sections like functions, conditionals, or file handling as well!
