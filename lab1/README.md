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

Input the comma-separated integers and transform them into a list of integers.
Print the number of even ints in the given list. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
Use a function of counting evens.

        count_evens([2, 1, 2, 3, 4]) → 3
        count_evens([2, 2, 0]) → 3
        count_evens([1, 3, 5]) → 0


#### Exercise 2

Input the comma-separated integers and transform them into a list of integers.
Return the "centered" average of an list of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the list. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the list is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3

#### Exercise 3

Input the comma-separated integers and transform them into a list of integers.
Given a list of ints, return True if the list contains a 2 next to a 2 somewhere.
