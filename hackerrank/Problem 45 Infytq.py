w1 = input()
w2 = input()

def max_length(s1, s2):
    max_ = ""
    while(s1<len(w1) and s2<len(w2)):
        if w1[s1]==w2[s2]:
            max_+=w1[s1]
        else:
            break
        s1+=1
        s2+=1
    return max_


res = ""
for i in range(len(w1)):
    for j in range(len(w2)):
        if w1[i]==w2[j]:
            temp = max_length(i, j)
            if len(temp)>len(res):
                res = temp

if len(res)==0:
    print(-1)
else:
    print(res)
