class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        temp = ''
        for i in range(n):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                temp+=s[i]
            else:
                
                if (s[i]==')' and len(temp)>0 and temp[-1]=='('):
                    temp = temp[:len(temp)-1]
                elif (s[i]==']' and len(temp)>0 and  temp[-1]=='['):
                    temp = temp[:len(temp)-1]
                elif (s[i]=='}' and len(temp)>0 and temp[-1]=='{'):
                    temp = temp[:len(temp)-1]
                else:
                    return False

        if len(temp)>0:
            return False
        return True
