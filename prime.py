num=int(input())
flag=False
if num>1:
    for i in range(2,num):
        if(i%2)==0:
            flag=True
            break
    if flag:
        print("It is not a prime")
    else:
        print("It is a prime")