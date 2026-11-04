
arr = ["add", '+', "sub", "-", "mul", "*", "div", "/", "mod", "%", "pow", "^"]

def calc(operator, a, b=None):
    if(a != None and b != None):
            try:
                if not (isinstance(a, (int, float))):
                    raise TypeError(f"Invalid number \"{a}\"")
            
                if not (isinstance(b, (int, float))):
                    raise TypeError(f"Invalid number \"{b}\"")
        
            
                if(operator ==  "add" or operator == '+'):
                    return a + b

                elif(operator == "sub" or operator == '-'):
                    return a - b

                elif(operator == "mul" or operator == '*'):
                    return a * b

                elif(operator == "div" or operator == '/'):
                    if (b == 0): 
                        raise ZeroDivisionError("Division by zero")
                    else:
                        return a / b

                elif(operator == "mod" or operator == '%'):
                    if (b != 0):
                        return a % b
                    else:
                        raise ZeroDivisionError("Division by zero")

                elif(operator == "pow" or operator == '^'):
                    return a ** b

                else:
                    raise UnboundLocalError(f"Invalid operator \"{operator}\"")

            except Exception as e:
                return str(e)
            
    else:
        if not (isinstance(a, (int, float))):
            return f"Invalid number \"{a}\""
        elif (operator not in arr):
            return f"Invalid operator \"{operator}\""
        elif (operator == "sub" or operator ==  "-"):
        # elif operator in ("sub" , "-"):
            return -a
        else:
            return a
    
def eval(lst1):
    
    if not isinstance(lst1, list):
        return f'Failed to evaluate "{lst1}"'

    if len(lst1) not in (2, 3):
        return f'Failed to evaluate "{lst1}"'
    
    operator = lst1[0]
    a = lst1[1]

    if isinstance(a, list):
            a = eval(a)
            if isinstance(a, str):
                return a
    
    if len(lst1) == 2:
            return calc(operator, a)
    
    else:
        b = lst1[2]

        if isinstance(b, list):
            b = eval(b)
            if isinstance(b, str):
                return b

        if (len(lst1) == 3 and
        lst1[0] in arr and
        isinstance(a, (int, float)) and
        isinstance(b, (int, float))):

            return calc(operator, a, b)

        return calc(operator, a, b )

def struct(struct_list):    

    if not isinstance(struct_list, list):
        return (f'Failed to structure \"{struct_list}\"')
    
    if (len(struct_list) == 0):
        return (f'Failed to structure "{struct_list}"')
    
    if len(struct_list) == 2:
        # if isinstance(struct_list[0], str) and struct_list[0] in arr:
        return struct_list
    
    if (len(struct_list) % 2 == 0):
        return (f'Failed to structure \"{struct_list}\"')
    
    for i, item in enumerate(struct_list):
        if i % 2 == 1:
            if not isinstance(item, str):
                return (f'Failed to structure \"{struct_list}\"')

    if len(struct_list) == 2:
        return struct_list
    
    if len(struct_list) == 1:
        if struct_list[0] in arr:
            return f'Failed to structure "{struct_list}"'
        return struct_list

    if len(struct_list) == 3 and struct_list[0] in arr:
        return struct_list    
    
    left = struct_list[0]
    operator = struct_list[1]
    right = struct_list[2]

    function_ops = ['^', 'pow']

    for i in range(len(struct_list)):

        if struct_list[i] in function_ops:

            left = struct_list[i-1]
            operator = struct_list[i]
            right = struct_list[i+1]

            before = struct_list[:i-1]
            middle = [operator, left, right]
            after = struct_list[i+2:]

            new_struct_list = before + [middle] + after

            if len(new_struct_list) == 1:
                return middle

            return struct(new_struct_list)
        
        
    level_one = ['*', '/', '%', 'mul', 'div', 'mod']
    for i in range(len(struct_list)):
        if struct_list[i] in level_one:
            left = struct_list[i-1]
            operator = struct_list[i]
            right = struct_list[i+1]

            before = struct_list[:i-1]
            middle = [operator, left, right]
            after = struct_list[i+2:]

            new_struct_list = before + [middle] + after
            if len(new_struct_list) == 1:
                return middle

            return struct(new_struct_list)

    # if len(struct_list) == 3:
    #     return [operator, left, right]
    
    # first = [operator, left, right]
    # remaining = struct_list[3:]
    # new_struct_list = [first] + remaining
    # return struct(new_struct_list)     

    level_two = ['+', 'add', '-', 'sub']
    for i in range(len(struct_list)):
        if struct_list[i] in level_two:
            left = struct_list[i-1]
            operator = struct_list[i]
            right = struct_list[i+1]

            before = struct_list[:i-1]
            middle = [operator, left, right]
            after = struct_list[i+2:]
            
            new_struct_list = before + [middle] + after

            if len(new_struct_list) == 1:
                return middle

            return struct(new_struct_list)
        
    for i in range(len(struct_list)):
        item = struct_list[i]

        if isinstance(item, str):

            left = struct_list[i - 1]
            operator = item
            right = struct_list[i + 1]

            before = struct_list[:i - 1]
            middle = [operator, left, right]
            after = struct_list[i + 2:]

            new_struct_list = before + [middle] + after

            if len(new_struct_list) == 1:
                return middle

            return struct(new_struct_list)
    

def get_next(s, start):
    if len(s) == 0 or start >= len(s):
        return "End of string"
    else:
        num = ""

        while start < len(s) and (s[start].isdigit() or s[start] == '.'):
            num += s[start]
            start += 1

        if num:    
            if '.' in num:
                return float(num)
            return int(num)

        else:
            op = ""

            while start < len(s) and not s[start].isdigit() and s[start] != '(' and s[start] != ')':
                op += s[start]
                start+=1

            return op

def parse(sr):
    sr = sr.replace(' ', '')
    result = []
    start = 0

    while start < len(sr):
        if sr[start] == '(':
            depth = 0
            end = start

            for i in range(start, len(sr)):
                if sr[i] == '(':
                    depth += 1
                elif sr[i] == ')':
                    depth -= 1
                    if depth == 0:
                        end = i
                        break 
            
            inner = sr[start + 1 : end]
            result.append(parse(inner))
            start = end + 1
            continue

        token = get_next(sr, start)

        if token == "End of string":
            break
        
        result.append(token)

    if not isinstance(token, (int, float)):
        start += len(str(token))
    else:
        start += len(str(token))

    return struct(result)

def pre_parse(sr1):
    counter = 0
    for i in range(len(sr1)):
        if sr1[i] == '(':
            counter += 1
        elif sr1[i] == ')':
            counter -= 1

    if counter > 0 or counter < 0:
        raise Exception("Not matching parenthesis")

def coordinate(strin):
    try:
        pre_parse(strin)
        parsed = parse(strin)

        if isinstance(parsed, str):
            raise Exception(parsed)
        
        result = eval(parsed)

        if isinstance(result, str):
            raise Exception(result)
        
        return result

    except Exception as e:
        return f'Error: {e}'

if __name__ == "__main__":
    while True:
        user_input = input()
        if user_input == 'q' or user_input == 'quit':
            break
        print(coordinate(user_input))