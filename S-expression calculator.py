# get the subpart of the expression
def start_end(expression):
    end_found = 0
    startindex = 0
    endindex = 0
    for i in range(len(expression)):
        if(expression[i] == ")" and end_found == 0):
            endindex = i
            while(i != -1):
                i -= 1
                if(expression[i] == "("):
                    startindex = i
                    end_found = -1
                    break
        if(end_found == -1):
            # return the start and end index of subpart of expression
            return (startindex, endindex)
        # return none where the brackets are unbalanced
    return (None, None)


def EvaluteExpression(input_expression):
    if(len(input_expression) >= 2):
        tmp_expression = input_expression
        print(tmp_expression)
        while(tmp_expression.count("(") > 0):
            (start, end) = start_end(tmp_expression)
            if(start != None and end != None):
                tmp_string = tmp_expression[start: end + 1][:-1][1:].split(" ")

                # multiplication
                if(tmp_string[0][0] == "m"):
                    mulresult = 1
                    for i in range(1, len(tmp_string)):
                        mulresult *= int(tmp_string[i])
                    tmp_expression = tmp_expression[:start] + \
                        str(mulresult) + tmp_expression[end + 1:]
                    print(tmp_expression)

                # addition
                elif(tmp_string[0][0] == "a"):
                    addresult = 0
                    for i in range(1, len(tmp_string)):
                        addresult += int(tmp_string[i])
                    tmp_expression = tmp_expression[:start] + \
                        str(addresult) + tmp_expression[end + 1:]
                    print(tmp_expression)

                else:
                    return "Expression contains operations which are not supported (Only add and multiply operations are supported now.)"
            else:
                return "Brackets are unbalanced, please check your expression."
        return "Expression evaluation is successful!"


if __name__ == '__main__':
    expression = '(multiply 2 (add (multiply 2 4) 5))'
    print(EvaluteExpression(expression))
