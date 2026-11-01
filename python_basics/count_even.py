def count_even(num):
    count=0
    for i in num:
        if i%2==0:
            count +=1
    return(count)
print(count_even([2,5,8,6]))