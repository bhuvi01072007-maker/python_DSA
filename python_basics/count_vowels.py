def count_vowels(name):
    count=0
    for i in name:
        if i in "AEIOUaeiou":
            count += 1
    return(count)
print(count_vowels("sara"))