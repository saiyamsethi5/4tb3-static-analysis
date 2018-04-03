#scanner.py
#Final Project - Group Number: 10
#Requirements: scanner requires a file named input_code.py containing the python3 grammer

import collections
from organized_dict import organized_dict
from filter_input import filter_input
from opt_modules.if_else_optimizer import if_else_optimizer


#function: scanner
#input: py_input - a list of python grammar retreived from input_code.py
#definition: iterates through each item in the list and scans for matching symbols
def scanner (py_input):
    #print (py_input)

    filter_code = filter_input (py_input)
    filtered_code = filter_code.filter_keywords()   #filters the code for specified keywords

    #print (filtered_code)
    opt1 = if_else_optimizer(filtered_code)
    opt1.search_for_optimization()


#function: main
#input: N/A
#definition: main function - reads from file into list - calls scanner
def main():

    i = 1;
    py_input = organized_dict(collections.OrderedDict())

    with open('input_code.py') as f:  #Reads input.txt file into list p0_input
        for lines in f.readlines():
            py_input [i] = lines.rstrip()  #stores line num : code in line (without the /n and without whitespaces)
            i = i + 1   #increments the line number

    scanner(py_input)

if __name__ == "__main__":
    main()