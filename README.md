# 🐍 Programming in Python

A structured collection of notes, examples, exercises, and practice programs covering the fundamentals of Python programming, from functions and variables to object-oriented programming and advanced Python features.

This repository follows a progressive learning path and is intended for beginners who want to build a strong foundation in Python.

---

## 📚 Course Contents

### Section 2 — Functions & Variables 🐍

* Setting up the environment with VS Code & CLI
* Hello, World! and the `print()` function
* Bugs and debugging syntax errors
* Interactivity with the `input()` function
* Variables and assignment
* Comments and pseudo-code
* String operations and concatenation
* Print parameters: `sep` and `end`
* String formatting, f-strings, and string methods
* Data types: Integers and basic arithmetic
* Data types: Floats and the `round()` function
* Defining custom functions with `def`
* Returning values from functions

---

### Section 3 — Conditionals 🔀

* Introduction to conditional operators
* `if` statements and Boolean expressions
* Chaining conditions with `elif`
* The `else` catchall
* Logical `or` operator
* Logical `and` operator
* Parity checking: odd/even
* Pythonic conditional code
* The `match` statement

---

### Section 4 — Loops 🔁

* The `while` loop
* Infinite loops and loop control
* The `for` loop
* Iterating over lists
* Lists data structure
* The `range()` function
* Pythonic underscore discard variable
* Dictionaries and key-value pairs
* Lists of dictionaries
* Nested loops
* Abstractions with grid-based problems such as Mario

---

### Section 5 — Exceptions ⚠️

* Syntax errors vs. runtime errors
* `try` and `except` blocks
* Handling `ValueError` and `NameError`
* The `else` block in exception handling
* Input validation loops
* The `pass` keyword
* Parameterizing error handlers

---

### Section 6 — Libraries 📚

* Modules and code reusability
* `import` syntax
* The `random` module

  * `choice()`
  * `randint()`
  * `shuffle()`
* The `statistics` module

  * `mean()`
* Command-line arguments with `sys.argv`
* Slicing lists and strings
* Third-party packages and `pip`
* APIs and web requests
* Working with JSON
* Creating custom modules

---

### Section 7 — Unit Tests 🧪

* Automated testing concepts
* The `assert` keyword
* The `pytest` framework
* Testing exceptions with `pytest.raises`
* Test packages
* `__init__.py` folders

---

### Section 8 — File I/O 📂

* Persistent storage concepts
* The `open()` function

  * Read
  * Write
  * Append
* File management with the `with` keyword
* Parsing flat text files
* Comma-Separated Values (CSV)
* Reading CSV files with `csv.reader`
* Reading CSV files with `csv.DictReader`
* Writing CSV files with `csv.writer`
* Handling binary files
* Working with images using the Pillow library

---

### Section 9 — Regular Expressions 🔤

* Pattern matching concepts
* Introduction to Regex
* The `re` library
* `re.search()`
* Regex quantifiers and metacharacters
* Escape sequences
* Raw strings
* Boundary anchors

  * `^` — start of string
  * `$` — end of string
* Character classes and ranges
* Regex shortcuts

  * Words
  * Digits
  * Whitespace
* Regex flags such as `IGNORECASE`
* Data extraction with capturing groups
* The walrus operator `:=`
* Non-capturing groups

---

### Section 10 — Object-Oriented Programming (OOP) 🏗️

* Programming paradigms
* Introduction to OOP
* Tuples and immutable data containers
* Classes and objects
* The `__init__` method
* Instance variables
* Raising exceptions
* The `__str__` special method
* Custom instance methods
* Properties, getters, and setters
* Class methods
* Class variables
* Inheritance
* The `super()` function
* Operator overloading

---

### Section 11 — Additional Features & Outro 🧰

* Sets data structure
* Global variables and scope
* Constants in Python
* Type hints
* Static type checking with `mypy`
* Docstrings
* Advanced command-line arguments with `argparse`
* Unpacking lists and dictionaries
* Variadic functions

  * `*args`
  * `**kwargs`
* The `map()` function
* List comprehensions
* The `filter()` function
* Generators
* The `yield` keyword
* Course outro and text-to-speech demonstration

---

## 🛠️ Technologies & Tools

* **Python**
* **VS Code**
* **Python CLI**
* **pip**
* **pytest**
* **mypy**
* **Pillow**
* **Regular Expressions**
* **JSON**
* **CSV**
* **APIs**

---

## 🚀 Getting Started

### 1. Install Python

Download and install Python from the official Python website.

Verify the installation:

```bash
python --version
```

or on some systems:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone <repository-url>
```

Navigate to the project:

```bash
cd <repository-name>
```

### 3. Run a Python Program

```bash
python filename.py
```

---

## 📦 Installing Packages

Python's built-in modules do not require installation.

For third-party packages, use `pip`:

```bash
pip install package-name
```

For example:

```bash
pip install pytest
```

```bash
pip install pillow
```

---

## 🧪 Running Tests

If the repository contains `pytest` tests:

```bash
pytest
```

You can also run:

```bash
python -m pytest
```

---

## 📁 Repository Structure

The repository is organized according to the concepts covered throughout the course.

```text
ProgrammingInPython/
│
├── Functions/
├── Conditionals/
├── Loops/
├── Exceptions/
├── Libraries/
├── UnitTests/
├── FileIO/
├── RegularExpressions/
├── OOP/
└── AdditionalFeatures/
```

> The exact folder structure may vary depending on how the exercises and programs are organized.

---

## 🎯 Learning Goals

By completing the programs and exercises in this repository, you will learn how to:

* Write and execute Python programs
* Work with variables and different data types
* Create reusable functions
* Implement conditional logic and loops
* Handle errors and exceptions
* Work with Python modules and external packages
* Process files, CSV data, and JSON
* Use regular expressions for pattern matching
* Write automated tests
* Understand object-oriented programming
* Use type hints and static type checking
* Work with generators and comprehensions
* Build command-line applications

---

## 💡 Key Python Concepts

Some of the major concepts covered include:

```python
# Functions
def hello(name):
    return f"Hello, {name}"
```

```python
# Conditionals
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

```python
# Loops
for i in range(5):
    print(i)
```

```python
# Exception handling
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
```

```python
# Regular expressions
import re

if re.search(r".+@.+\.edu", email):
    print("Valid")
```

```python
# Classes
class Student:
    def __init__(self, name):
        self.name = name
```

---

## 📈 Learning Progress

* [ ] Functions & Variables
* [ ] Conditionals
* [ ] Loops
* [ ] Exceptions
* [ ] Libraries
* [ ] Unit Tests
* [ ] File I/O
* [ ] Regular Expressions
* [ ] Object-Oriented Programming
* [ ] Additional Python Features

---

## 🤝 Purpose

This repository serves as a personal learning record and reference for Python programming concepts, examples, and exercises.

It can also be used as a reference for revising Python fundamentals and preparing for coding interviews.

---

## 📝 Notes

The examples in this repository are focused on understanding **how Python works**, rather than simply memorizing syntax.

The goal is to gradually move from basic Python syntax to writing cleaner, reusable, testable, and more Pythonic code.

---

## 👩‍💻 Author

**Nandini Amaravadi**

Learning Python and building a strong foundation in programming, problem solving, and software development, AI Engineering.
