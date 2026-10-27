class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        my_stack = deque()

        for ch in s:
            if ch in pairs.keys():
                if my_stack and my_stack[-1] == pairs[ch]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(ch)
        print(my_stack)
        return len(my_stack) == 0
