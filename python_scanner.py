#scanner.py
#Final Project - Group Number: 10
#Requirements: scanner requires a file named input_code.py containing the python3 grammer

#Dictionary of supported symbols and their appropriate outputs
optimized = {'if':'IF_SYM', 'else': 'ELSE_SYM'}


#function: scanner
#input: py_input - a list of python grammar retreived from input_code.py
#definition: iterates through each item in the list and scans for matching symbols
def scanner (py_input):
    print (py_input)


#function: main
#input: N/A
#definition: main function - reads from file into list - calls scanner
def main():

    i = 1;
    py_input = {}

    with open('input_code.py') as f:  #Reads input.txt file into list p0_input
        for lines in f.readlines():
            py_input [i] = lines.rstrip().replace(" ", "")   #stores line num : code in line (without the /n and without whitespaces)
            i = i + 1   #increments the line number

    scanner(py_input)

if __name__ == "__main__":
    main()