
arr = list(map(int, input(', ').split(', ')))

m = int(input())

def distrb(arr, m):
    arr = sorted(arr)
    print(arr)
    min_diff = arr[m]-arr[0]
    for i in range(len(arr)-m+1):
        min_diff = min(min_diff, arr[i+m-1]-arr[i])
    return min_diff
    
print(distrb(arr, m))
