def find_max(num):
    biggest=num[0]
    for i in num:
        if i>biggest:
            biggest=i
    return(biggest)
print(find_max([4,1,6,9]))
