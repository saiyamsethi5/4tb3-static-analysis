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

Concept and Limitations:
The scanner itself is designed to scan the input code and store line by line into a dictionary. For example {'1': line_1_code, '2': line_2_code...}
The scanner then filters this dictionary for key words (if, for, else, etc.) and removes any code that would not be required for the optimizer.
Using the filtered dictionary, each optimization module is called to see if there is a technique that can be applied.

The program is not perfect but works for many scenarios. The limitations that can be applied are:
- for loops: Python has a diffrent way of using for loops - so we decided to only analyze for loops that utilize 'range' - such as: for x in range (0, 10)
- 2 individual for loops may be thought of as nested: Because the scanner discards of any unecessary code, it is difficult to keep track of where the foor loop starts and ends.
This is why 2 conesecutive for loops may be thought of as nested.

Additional Information:

python_scanner.py:
    The main program that scans a provided python file into a dictionary and proceeds to filter and search for possible optimizations

output_message.py:
    A class that is used to perform the output of the program and display optimization techniques

organized_dict.py:
    A wrapper class for use on top with the OrderedDict class that allows returning of the next item in an ordered dictionary provided the index

filter_input.py:
    A class that takes the input code dictionary and returns a filtered dictionary containing those lines of codes with specified keywords (if, for, else, etc)

opt_modules:

nested_for_optimizer.py:
    A class that searches for possible optimizations on nested for loops and calls the output_message class to identify detailed techniques

if_else_optimizer.py:
    A class that searches for possible optimizations on if-else satements and calls the output_message class to identify detailed techniques

avoid_multuply_optimizer.py:
    A class that searches for possible optimizations on multiplication techniques and calls the output_message class to identify detailed techniques

loop_overhead_optimizer.py:
    A class that searches for possible optimizations on for loops and calls the output_message class to identify detailed techniques