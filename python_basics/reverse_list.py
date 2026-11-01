def reverse_list(num):
    result=[]
    for i in range(len(num)-1,-1,-1):
        result.append(num[i])
    return(result)
print(reverse_list([1,2,3,4,5]))