def has_duplicates(num):
    seen={}
    for i in num:
        if i in seen:
            return True
        seen[i]=True
    return False
print(has_duplicates([4,1,7,4]))
print(has_duplicates([4,1,7,6]))
print(has_duplicates([]))
