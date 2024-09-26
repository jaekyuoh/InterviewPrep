class Solution:
    def isValid(self, s: str) -> bool:
        complements = {")": "(", "}": "{", "]": "["}
        stack = [s[0]]
        for ch in s[1:]:
            if ch in complements:
                if len(stack) > 0 and stack[-1] == complements[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0

if __name__ == '__main__':
    s = "{[]}"
    s2 = "(){}}{"
    stack = []
    complements = {"(": ")", "{": "}", "[": "]"}
    print(s[1:])
    print(complements["("])
