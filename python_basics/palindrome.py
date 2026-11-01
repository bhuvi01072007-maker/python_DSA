def palindrome(word):
    word=word.lower()
    reversed_word=""
    for i in range(len(word)-1,-1,-1):
        reversed_word +=word[i]
    return word==reversed_word
print(palindrome("madam"))