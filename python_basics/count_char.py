def count_char(name):
    count={}
    for i in name:
        if i in count:
            count[i] +=1
        else:
            count[i]=1
    return(count)
print(count_char("bhuvana"))