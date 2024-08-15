def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems is too many
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    for i, problem in enumerate(problems):
        # Split the problem into its components
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        # Check for valid operators
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        # Check if operands are digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check if operands are within the limit
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the width of the problem for formatting
        width = max(len(num1), len(num2)) + 2
        
        # Build the lines for output
        first_line += str(num1).rjust(width)
        second_line += operator + str(num2).rjust(width - 1)
        dashes += "-" * width
        
        # Calculate the answer if required
        if show_answers:
            if operator == "+":
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers += answer.rjust(width)
        
        # Add spacing between problems (except after the last one)
        if i < len(problems) - 1:
            first_line += "    "
            second_line += "    "
            dashes += "    "
            if show_answers:
                answers += "    "
    
    # Combine the lines into the final output
    arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    if show_answers:
        arranged_problems += "\n" + answers
    
    return arranged_problems
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# Output:
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
# Output:
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
# Output: "Error: Too many problems."

print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# Output: "Error: Operator must be '+' or '-'."

print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
# Output: "Error: Numbers cannot be more than four digits."

print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
# Output: "Error: Numbers must only contain digits."
