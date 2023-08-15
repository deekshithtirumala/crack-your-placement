keys = list(map(int, input().split()))
paper = list(map(int, input().split()))

def score(keys, paper):
    marks = 0
    for i in range(len(keys)):
        if keys[i]==paper[i]:
            marks+=3
        elif paper[i]!=-1:
            marks-=1
            
    return marks

print(score(keys, paper))
