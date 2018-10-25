distro_dict ={
    2:1,
    3:2,
    4:3,
    5:4,
    6:5,
    7:6,
    8:5,
    9:4,
    10:3,
    11:2,
    12:1
}

def check(a,b,n):
    counter =0
    for a_item in a:
        for b_item in b:
            if a_item + b_item == n:
                counter+=1

    return counter


def recursive(a,b,n):
    val = check(a,b,n)
    if(val>distro_dict[n]):
        pass
    elif(val<distro_dict[n]):
        recursive(a+[n-1],b,n)
        recursive(a, b +[n-1], n)
    else:
        if(n==12):
            if(len(a)==6 and len(b)==6 and a!=[1,2,3,4,5,6]):
                print(a)
                print(b)
        else:
            recursive(a,b,n+1)


recursive([1],[1],2)
