n = input()

def check(num, n):
    _max = 0
    for i in range(n-1):
        for j in range(i, n):
            temp = num[i:j+1]
            #print(temp)
            if isValid(temp):
                _max = max(_max, len(temp))
    return _max
def sum_(num):
    num = int(num)
    res = 0
    while num>0:
        res+=num%10
        num = num//10
    return res
def isValid(num):
    if len(num)%2!=0:
        return False
    if sum_(num[:len(num)//2])==sum_(num[len(num)//2:]):
        return True
    return False

print(check(n, len(n)))
