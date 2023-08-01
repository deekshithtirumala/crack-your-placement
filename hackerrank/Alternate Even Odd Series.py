word = input()

even = []
odd = []
count = 0
for i in word:
    if i.isdigit():
        if int(i)%2==0:
            even.append(int(i))
        else:
            odd.append(int(i))
    elif  not i.isalpha():
        count+=1
#print(count)

for i in range(max(len(even), len(odd))):
    if count%2==0:
        if i<len(even):
            print(even[i], end='')
        if i<len(odd):
            print(odd[i], end='')
    else:
        if i<len(odd):
            print(odd[i], end='')
        if i<len(even):
            print(even[i], end='')
