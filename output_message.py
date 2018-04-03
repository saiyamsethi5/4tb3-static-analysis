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
        print ("\tIf else can be optimized: ")
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

    def avoid_mult_msg (line_num, loop_code):
        print("Line " + str(line_num) + ": ")
        print ("\tMultiplication can bes optimized in for loop - " + loop_code)
        print ("\n")

    def loop_overhead_msg (line_num, loop_code):
        print("Line " + str(line_num) + ": ")
        print ("\tFor loop can be optimized using negative while - " + loop_code)
        print ("\n")
