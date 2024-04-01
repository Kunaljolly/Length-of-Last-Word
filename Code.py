class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s[::-1])
        print(s)
        c = 0
        for x in range(len(s)-1):
            if s[x] != ' ' and s[x+1] == ' ':
                return c+1
            if s[x] != ' ':
                c += 1
        return c+1
            

