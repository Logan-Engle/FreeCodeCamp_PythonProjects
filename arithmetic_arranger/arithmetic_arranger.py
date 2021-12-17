import re

def arithmetic_arranger(problem_list, answer_flag=False):
    """
    Given a list of up to 5 basic addition or subtraction problems
    formats the problems like one would in primary school all and
    provides answers when the answer flag is set to true
    """
    
    first_line = ""
    second_line = ""
    equals_line = ""
    answer_line = ""

    # Error catching for more than 5 problems
    if len(problem_list) > 5:
        return "Error: Too many problems."

    for problem in problem_list:
        # Error catching for incorrect characters
        if problem in problem_list:
            if re.search("[^\s0-9.+-]", problem):
                if re.search("[/]", problem) or re.search("[*]", problem):
                    return "Error: Operator must be '+' or '-'."
                return "Error: Numbers must only contain digits."

        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        # Error catching for numbers over 4 digits
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if operator == "+":
            calculation = str(int(first_number) + int(second_number))
        elif operator == "-":
            calculation = str(int(first_number) - int(second_number))

        # sets correct string lengths and aligns to the right
        string_length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(string_length )
        bottom = operator + str(second_number).rjust(string_length - 1)
        answer = str(calculation).rjust(string_length)
        equals = "-" * string_length

        # handles spacing between problems
        if problem != problem_list[-1]:
            first_line  += f"{top}    "
            second_line += f"{bottom}    "
            equals_line += f"{equals}    "
            answer_line += f"{answer}    "
        else:
            first_line  += top    
            second_line += bottom 
            equals_line += equals 
            answer_line += answer 

    # outputs depending on answer flag
    if answer_flag:
        string = f"{first_line}\n{second_line}\n{equals_line}\n{answer_line}"
    else:
        string = f"{first_line}\n{second_line}\n{equals_line}"
        
    return string