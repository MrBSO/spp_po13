def is_valid_brackets(s):
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != brackets[char]:
                print(False)
                return
            stack.pop()
    
    print(len(stack) == 0)

s = input()
is_valid_brackets(s)