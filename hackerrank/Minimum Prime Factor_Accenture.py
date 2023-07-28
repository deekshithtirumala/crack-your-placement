n = int(input())

def isPrime(num):
    
    for i in range(2, int(num**0.5)):
        if num%i==0:
            return False
    return True
for i in range(2,int(n**0.5)+1):
    if n%i==0 and isPrime(i):
        print(n-i)
        break
else:
    print(0)
