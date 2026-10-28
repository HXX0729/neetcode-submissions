class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '*', '/'}
        for t in tokens:
            if t in op:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == '+':
                    res = a + b
                elif t == '*':
                    res = a * b
                elif t == '-':
                    res = a - b
                else:
                    res = a / b
                stack.append(res)
            else:
                stack.append(t)
            #print(stack)
        return int(stack[0])