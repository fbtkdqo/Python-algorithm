def isValid(slef, s: str) -> bool:
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    # 예외처리 및 일치 여부
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
        return len(stack) == 0