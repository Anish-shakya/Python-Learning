# 📘 Welcome to My Python Learning Journey! 🚀
Hello there! 👋 I'm Anish, and I'm on an exciting journey to become a Data Analyst using Python! 🐍📊

This repository is my personal learning tracker, where I document everything I learn about Python, data analysis, and related technologies. 
Whether it's coding basics, data manipulation, visualization, or machine learning, I'll be sharing my progress here.
# Table Of Content
# Basics
## Comments
## Variables
## DataTypes
## Strings 
# Dictionary and Sets
# List and Tuples
# Loops
# Functions

### 1. What is a Function?

A **function** is a block of code that performs a specific task.  
You use functions to avoid repeating code and to make your code more organized and reusable.

---

### 2. Why Use Functions?

- To **reuse code** instead of writing the same thing again and again.
- To **organize** code better.
- To make your code more **modular** and easier to test or debug.

---

### 3. How to Create a Function

In Python, you create a function using the `def` keyword.  
Here is the basic structure:

```python
def function_name():
    # code inside the function
    print("This is a function.")
```

---

### 4. How to Call a Function

To use the function, you need to **call** it:

```python
function_name()
```

---

### 5. Example: Simple Function

```python
def say_hello():
    print("Hello!")

say_hello()   # Output: Hello!
```

---

### 6. Function with Parameters

You can pass values (called **arguments**) to a function.

```python
def greet(name):
    print("Hello", name)

greet("John")   # Output: Hello John
```

Here, `name` is called a **parameter**.

---

### 7. Function with Multiple Parameters

```python
def add(a, b):
    result = a + b
    print("Sum is", result)

add(3, 5)   # Output: Sum is 8
```

---

### 8. Function that Returns a Value

Sometimes, you want the function to send back a result. Use `return`.

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)   # Output: 20
```

---

### 9. Default Parameter Values

If you want to give a default value in case no argument is passed:

```python
def greet(name="Guest"):
    print("Hello", name)

greet()        # Output: Hello Guest
greet("Rita")  # Output: Hello Rita
```

---

### 10. Keyword Arguments

You can also pass arguments using the parameter names:

```python
def divide(a, b):
    return a / b

print(divide(b=10, a=20))  # Output: 2.0
```

---

### 11. *args and **kwargs (Advanced but simple explanation)

If you don’t know how many arguments will be passed:

#### Using `*args` for multiple positional arguments:
```python
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3, 4)   # Output: 10
```

#### Using `**kwargs` for multiple keyword arguments:
```python
def show_info(**data):
    for key, value in data.items():
        print(key, ":", value)

show_info(name="Rita", age=25)
# Output:
# name : Rita
# age : 25
```

---

### 12. Scope of Variables in Functions

Variables inside a function are **local** to that function.

```python
def test():
    x = 10
    print(x)

test()
# print(x)  # This will cause an error, because x is not accessible outside the function
```

---

# Object Oriented Programming Concept
OOPs is a programming paradigm based on the concept of "objects", which contain data and methods to operate on that data.

## 4 Main Pillars of OOPs
### Encapsulation
- Bundling of data (attributes) and methods inside a class.

- Helps protect internal object details from outside interference.

### Abstraction

- Hiding complex implementation details and showing only essential features.

- Achieved using methods and classes.

### Inheritance

- One class (child) inherits attributes and methods from another class (parent).

- Promotes code reusability.

### Polymorphism

- Same method name behaving differently in different classes.

- "Many forms" – one interface, many implementation

## Class and Objects
### **Class**
A **class** is like a blueprint for creating **objects**. It defines the structure and behavior (data and functions) that the created objects will have.

- It can contain attributes (variables) and methods (functions).
- Think of it as a template. For example, a `Car` class defines what a car is, but no specific car exists until you create an object of that class.

### **Object**
An **object** is an instance of a class. It holds actual data and can use the methods defined in the class.

- Each object can have different values for the same attributes.
- Multiple objects can be created from the same class.

---

### 🧠 Key Terms
- **`__init__` method**: A special method called automatically when a new object is created. It's used to initialize object properties.
- **`self`**: Refers to the current instance of the class. Used to access variables and methods within the class.

---

### ✅ Example

```python
# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Create objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access methods
person1.greet()   # Output: Hello, my name is Alice and I'm 25 years old.
person2.greet()   # Output: Hello, my name is Bob and I'm 30 years old.
```

---
