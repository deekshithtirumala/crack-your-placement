n = int(input())

lst = list(set(map(int, input().split())))

lst = sorted(lst)
#print(lst)
res = 1
temp = 1
for i in range(len(lst)-1):
    if lst[i]+1==lst[i+1]:
        temp+=1
    else:
        res = max(res, temp)
        temp =1
        
res = max(res, temp)

print(res)
