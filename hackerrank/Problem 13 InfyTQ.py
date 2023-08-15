x, y, z = map(int, input().split(','))

def chk(x, y, z):
    lst = sorted([abs(x-y), abs(y-z), abs(x-z)])
    
    if lst[0]<=1 and lst[1]>1 and lst[2]>1:
        return True
    return False

print(chk(x, y, z))
    
