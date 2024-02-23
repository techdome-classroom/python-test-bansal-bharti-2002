class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in brackets_map.values():
                stack.append(char)
            elif char in brackets_map.keys():
                if not stack or brackets_map[char] != stack.pop():
                    return False
            else:
                return False
        
        return len(stack) == 0

  

