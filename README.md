## 📘 Welcome to My Python Learning Journey! 🚀
Hello there! 👋 I'm Anish, and I'm on an exciting journey to become a Data Analyst using Python! 🐍📊

This repository is my personal learning tracker, where I document everything I learn about Python, data analysis, and related technologies. 

Whether it's coding basics, data manipulation, visualization, or machine learning, I'll be sharing my progress here.

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

Do you want to try writing a function yourself? I can check it or guide you with examples.
