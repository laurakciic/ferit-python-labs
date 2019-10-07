# Lab 1

## Interactive tutorial

For details see: [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)

1. Some Python intro
1. Using the Python Interpreter
    1. Invoking the Interpreter
1. An Informal Introduction to Python
    1. Simple data-types
        1. Numbers
        2. Strings
        3. Lists
1. More Control Flow Tools
    1. ` if ` Statements
    2. ` for ` Statements
    3. The ` range() ` Function
    4. ` break ` and ` continue ` Statements, and ` else ` Clauses on Loops
    5. ` pass ` Statements
    6. Defining Functions
    7. More on Defining Functions
    8. Intermezzo: Coding Style
1. Python IDEs and VMs
1. Data Structures
    1. More on Lists
    1. The ` del ` Statement
    1. Tuples and Sequences
    1. Sets
    1. Dictionaries
    1. Looping Techniques
    1. More on Conditions
    1. Comparing Sequences and Other Types


## Interactive exercises

Selected exercises from [PracticePython.org](https://www.practicepython.org/)

- 1-10, 13, 24

## Your own work

#### Exercise 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).

The numbers obtained should be printed in a comma-separated sequence on a single line.

#### Exercise 2

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.

Suppose the following input is supplied to the program:

        8

Then, the output should be:

        40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

#### Exercise 3

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

Suppose the following input is supplied to the program:

        8

Then, the output should be:

        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

#### Exercise 4

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

Suppose the following input is supplied to the program:

        34,67,55,33,12,98

Then, the output should be:

        ['34', '67', '55', '33', '12', '98']
        ('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
