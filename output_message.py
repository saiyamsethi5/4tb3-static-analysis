#output_message.py
#Final Project - Group Number: 10
#Requirements: class to define the output message for individual optimization

class output_message:
    def nested_for_msg (line_num, loop_code, second_loop_code):
        print("\x1b[1;31mLine " + str(line_num) + ": \x1b[0m")
        print("\tNested for loop can be optimized: ")
        print ("\t" + loop_code)
        print ("\t\t" + second_loop_code)

        loop_lower_range = (loop_code.split("(")[1].split(",")[0])
        loop_code_upper_range = (loop_code.split(",")[1].split(")")[0])
        second_loop_code_upper_range = (second_loop_code.split(",")[1].split(")")[0])
        print ("\n\t\x1b[1;30mConsider the Following:\x1b[0m")
        print ("\tfor i in range (" + loop_lower_range + "," + loop_code_upper_range + " *" + second_loop_code_upper_range + ")")
        print ("\n")

    def if_else_msg (line_num, if_code, else_code):
        print("\x1b[1;31mLine " + str(line_num) + ": \x1b[0m")
        print ("\tIf-else can be optimized: ")
        print ("\t" + if_code)
        print ("\t\t" + "Case A")
        print ("\t" + else_code)
        print ("\t\t" + "Case B")
        print ("\n\t\x1b[1;30mConsider the Following:\x1b[0m")
        print ("\tCase B")
        print ("\t" + if_code)
        print ("\t\t" + "Undo Case B")
        print ("\t\t" + "Case A")
        print ("\n")

    def avoid_mult_msg (line_num, loop_code, mult_case):
        print("\x1b[1;31mLine " + str(line_num) + ": \x1b[0m")
        print ("\tMultiplication can be optimized: ")
        print ("\t" + loop_code)
        print ("\t" + mult_case)
        print ("\n\t\x1b[1;30mConsider the Following:\x1b[0m")
        loop_lower_range = (loop_code.split("(")[1].split(",")[0])
        for_loop_mult = loop_code.split(",")[1].split(")")[0]
        main_code_mult = mult_case.split("*")[1].split(")")[0]
        print("\tfor i in range (" + loop_lower_range + "," + for_loop_mult + "*" + main_code_mult + ")")
        print("\t" + str(mult_case.split("*")[0]) + ")")
        print ("\n")

    def loop_overhead_msg (line_num, loop_code):
        print("\x1b[1;31mLine " + str(line_num) + ": \x1b[0m")
        print ("\tLoop overhead can be optimized: ")
        print ("\t" + loop_code)
        print("\t\tLOOP CODE")

        loop_lower_range = (loop_code.split("(")[1].split(",")[0])
        loop_code_upper_range = (loop_code.split(",")[1].split(")")[0])
        print ("\n\t\x1b[1;30mConsider the Following:\x1b[0m")
        print ("\ti = " + str(int(loop_code_upper_range)-1))
        print("\tdo{")
        print("\t\tLOOP CODE")
        print("\t\ti = i - 1")
        print("\t} while (i >= " + loop_lower_range + ")")
        print ("\n")
