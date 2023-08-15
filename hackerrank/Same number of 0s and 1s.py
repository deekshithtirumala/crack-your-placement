n = int(input())

lst = list(map(int, input().split()))

level = 0
prev = 0
dic = {}
max_ = 0
for i in range(len(lst)):
    if level not in dic:
        dic[level]=i
    if lst[i]==0:
        level-=1
    elif lst[i]==1:
        level+=1
    #print(level, i, lst[i])
    if level in dic:
        #print(dic)
        max_ = max(max_, i-dic[level]+1)
        #print(max_, i, dic[level])
print(max_)
