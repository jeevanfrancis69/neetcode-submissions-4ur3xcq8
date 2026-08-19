class Solution:
    def isValid(self, s: str) -> bool:
        paranDict = {")" : "(" , "}" : "{" , "]" : "["}
        stack = []

        for char in s:
            if char in paranDict:
                #check if stack is not empty to pop the latest element
                if len(stack) != 0 and paranDict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False


