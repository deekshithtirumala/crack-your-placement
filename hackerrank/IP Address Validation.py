n = int(input())
def isipv4(num):
    lst = list(num.split('.'))
    if len(lst)!=4:
        return False
    for i in lst:
        if not i.isdigit():
            return False
        elif int(i)<0 or int(i)>255:
            return False
    return True

def checkhex(s):
    for i in s:
        if i not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']:
            return False
    return True
def isipv6(num):
    lst = list(num.split(':'))
    if len(lst)!=8:
        return False
    #print(lst)
    for i in lst:
        if len(i)>4:
            return False
        if (not checkhex(i)):
            #print(i)
            return False
    return True

for i in range(n):
    data = input()
    #print(data, end="  ")
    if isipv4(data):
        print("IPv4")
    elif isipv6(data):
        print("IPv6")
    else:
        print("Neither")
