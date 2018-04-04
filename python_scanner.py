#python_scanner.py
#Final Project - Group Number: 10
#Requirements: scanner requires a file named input_code.py containing the python3 grammer

import collections
from organized_dict import organized_dict
from filter_input import filter_input
from opt_modules.if_else_optimizer import if_else_optimizer
from opt_modules.nested_for_optimizer import nested_for_optimizer
from opt_modules.avoid_multiply_optimizer import avoid_multiply_optimizer
from opt_modules.loop_overhead_optimizer import loop_overhead_optimizer

#function: scanner
#input: py_input - an ordered dictionary of line numbers and python grammar retreived from input_code.py
#definition: filter codes and calls optimization modules for checking
def scanner (py_input):

    filter_code = filter_input (py_input)
    filtered_code = filter_code.filter_keywords()   #filters the code for specified keywords

    opt1 = nested_for_optimizer(filtered_code)
    opt1.search_for_optimization()

    opt2 = if_else_optimizer(filtered_code)
    opt2.search_for_optimization()

    opt3 = avoid_multiply_optimizer(filtered_code)
    opt3.search_for_optimization()

    opt4 = loop_overhead_optimizer(filtered_code)
    opt4.search_for_optimization()


#function: main
#input: N/A
#definition: main function - reads from file into ordered dict - calls scanner
def main():

    i = 1;
    py_input = organized_dict(collections.OrderedDict())

    with open('input_code.py') as f:  #Reads input_code.py file into ordered dictionary
        for lines in f.readlines():
            py_input [i] = lines.rstrip()  #stores line num : code in line (without the /n and without whitespaces)
            i = i + 1   #increments the line number

    scanner(py_input)

if __name__ == "__main__":
    main()