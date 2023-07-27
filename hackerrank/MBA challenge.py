num = input()
k = input()

if k=='0':
    print(1)
else:
    k = (int(k[len(k)-2:])%4)+4
    num = int(num[-1])
    print(str(num**k)[-1])
    
    
