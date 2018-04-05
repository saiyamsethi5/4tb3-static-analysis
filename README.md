# 4tb3-static-analysis
COMP SCI 4TB3 Final Project

The static analysis program consists of a Python3 scanner that given a provided python file as input - scans and returns suggesstions for a variety of cases of optimization that include:
- Nested For Loops
- If Else
- Multiplication
- Loop Overhead

To run the optimizer, required is a piece of python3 code in the root directory - must be named 'input_code.py'
A sample code that covers the base cases of each optimization technique can be found in the root directory under the name 'input_code.py'

Run the python_scanner.py code using a python 3 terminal or python 3 IDE.
This can be achieved by running 'python3 python_scanner.py'

Additional Source Code Information:

python_scanner.py:
    The main program that scans a provided python file into a dictionary and proceeds to filter and search for possible optimizations

output_message.py:
    A class that is used to perform the output of the program and display optimization techniques

organized_dict.py:
    A wrapper class for use on top with the OrderedDict class that allows returning of the next item in an ordered dictionary provided the index

filter_input.py:
    A class that takes the input code dictionary and returns a filtered dictionary containing those lines of codes with specified keywords (if, for, else, etc)

src/opt_modules:

nested_for_optimizer.py:
    A class that searches for possible optimizations on nested for loops and calls the output_message class to identify detailed techniques

if_else_optimizer.py:
    A class that searches for possible optimizations on if-else satements and calls the output_message class to identify detailed techniques

avoid_multuply_optimizer.py:
    A class that searches for possible optimizations on multiplication techniques and calls the output_message class to identify detailed techniques

loop_overhead_optimizer.py:
    A class that searches for possible optimizations on for loops and calls the output_message class to identify detailed techniques