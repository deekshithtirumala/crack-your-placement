class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            temp = i
            for j in range(len(needle)):
                if haystack[temp]==needle[j]:
                    temp+=1
            if temp-i==len(needle):
                return i
        else:
            return (-1)
