class output_message:
    def nested_for_msg (line_num, loop_code, second_loop_code):
        print("Line " + str(line_num) + ": ")
        print("\tNested for loop can be optimized: ")
        print ("\t" + loop_code)
        print ("\t\t" + second_loop_code)

        loop_lower_range = (loop_code.split("(")[1].split(",")[0])
        loop_code_upper_range = (loop_code.split(",")[1].split(")")[0])
        second_loop_code_upper_range = (second_loop_code.split(",")[1].split(")")[0])
        print ("\n\tConsider the Following:")
        print ("\tfor i in range (" + loop_lower_range + "," + loop_code_upper_range + " *" + second_loop_code_upper_range + ")")
        print ("\n")

    def if_else_msg (line_num, if_code, else_code):
        print("Line " + str(line_num) + ": ")
        print ("\tIf-else can be optimized: ")
        print ("\t" + if_code)
        print ("\t\t" + "Case A")
        print ("\t" + else_code)
        print ("\t\t" + "Case B")
        print("\n\tConsider the Following:")
        print ("\tCase B")
        print ("\t" + if_code)
        print ("\t\t" + "Undo Case B")
        print ("\t\t" + "Case A")
        print ("\n")

    def avoid_mult_msg (line_num, loop_code, mult_case):
        print("Line " + str(line_num) + ": ")
        print ("\tMultiplication can be optimized in for loop: ")
        print ("\t" + loop_code)
        print ("\t" + mult_case)
        print("\n\tConsider the Following:")
        loop_lower_range = (loop_code.split("(")[1].split(",")[0])
        for_loop_mult = loop_code.split(",")[1].split(")")[0]
        main_code_mult = mult_case.split("*")[1].split(")")[0]
        print("\tfor i in range (" + loop_lower_range + "," + for_loop_mult + "*" + main_code_mult + ")")
        print("\t" + str(mult_case.split("*")[0]) + ")")
        print ("\n")

    def loop_overhead_msg (line_num, loop_code):
        print("Line " + str(line_num) + ": ")
        print ("\tFor loop can be optimized using negative while: ")
        print ("\t" + loop_code)
        print("\t\tLOOP CODE")

        loop_lower_range = (loop_code.split("(")[1].split(",")[0])
        loop_code_upper_range = (loop_code.split(",")[1].split(")")[0])
        print("\n\tConsider the Following:")
        print ("\ti = " + str(int(loop_code_upper_range)-1))
        print("\tdo{")
        print("\t\tLOOP CODE")
        print("\t\ti = i - 1")
        print("\t} while (i >= " + loop_lower_range + ")")
        print ("\n")
