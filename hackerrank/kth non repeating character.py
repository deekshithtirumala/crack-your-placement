lst = list(input())
index = int(input())

dic = {}

for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
res = ""
for i in dic:
    if dic[i]==1:
        res+=str(i)

if len(res)<index:
    print(-1)
else:
    print(res[index-1])
