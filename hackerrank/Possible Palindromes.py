def max_palindrome(word):
    if word=='':
        return 0
    if word==word[::-1]:
        return 1
    max_length = 0
    max_word = ''
    left = ''
    right = ''
    for i in range(len(word)):
        for j in range(i+max_length, len(word)):
            temp = word[i:j+1]
            if temp==temp[::-1] and max_length<len(temp):
                max_length = len(temp)
                left = word[:i]
                right = word[j+1:]
                max_word = temp
    res = 1
    res+=max_palindrome(left)
    res+=max_palindrome(right)
    return res

print(max_palindrome(input()))
