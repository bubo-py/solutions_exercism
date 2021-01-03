def is_paired(input_string):
    pairs = {
        ']':'[',
        '}':'{',
        ')':'('
        }

    left_side = pairs.values()
    right_side = pairs.keys()
    stack = []
    
    for char in input_string:
        if char in left_side:
            stack.append(char)
        elif char in right_side:
            if not stack or stack[-1] != pairs[char]:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
