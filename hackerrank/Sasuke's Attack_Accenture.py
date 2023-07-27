n = int(input())
lst = list(map(int, input().split()))
k = int(input())

def sub(arr, k):
    new_arr = []
    
    for i in arr:
        i -=k

        new_arr.append(max(i, 0))
    return new_arr


new_arr = sub(lst, k)
    
print(max(new_arr))
