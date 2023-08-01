def sumOfDigits(num):
    tot = 0
    while num>0:
        tot+=num%10
        num//=10
    return tot

def permutations(num):
    return num*(num-1)//2
lst = list(set(map(int, input().split(','))))

count =0 
dic = {}
for i in range(len(lst)):
    if sumOfDigits(lst[i]) in dic:
        dic[sumOfDigits(lst[i])]+=1
    else:
        dic[sumOfDigits(lst[i])] = 1
        
total = 0
for i in dic.keys():
    total+=permutations(dic[i])
    
print(total)
