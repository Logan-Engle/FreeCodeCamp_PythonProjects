import re

def arithmetic_arranger(problem_list, answer_flag=False):
    """
    Arranges basic arithmetic as one would in primary school
    and provides the answers when second parameter set to true
    """
    first_line = ""
    second_line = ""
    equals_line = ""
    answer_line = ""
    string = ""

    if len(problem_list) > 5:
        return "Error: Too many problems."

    for problem in problem_list:

        if problem in problem_list:
            if re.search("[^\s0-9.+-]", problem):
                if re.search("[/]", problem) or re.search("[*]", problem):
                    return "Error: Operator must be '+' or '-'."
                return "Error: Numbers must only contain digits."

        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if operator == "+":
            calculation = str(int(first_number) + int(second_number))
        elif operator == "-":
            calculation = str(int(first_number) - int(second_number))

        string_length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(string_length )
        bottom = operator + str(second_number).rjust(string_length - 1)
        answer = str(calculation).rjust(string_length)
        equals = "-" * string_length

        if problem != problem_list[-1]:
            first_line +=  top    + '    '
            second_line += bottom + '    '
            equals_line += equals + '    '
            answer_line += answer + '    '
        else:
            first_line +=  top    
            second_line += bottom 
            equals_line += equals 
            answer_line += answer 

    if answer_flag:
        string = first_line + "\n" + second_line + "\n" + equals_line + "\n" + answer_line
    else:
        string = first_line + "\n" + second_line + "\n" + equals_line
        
    return string