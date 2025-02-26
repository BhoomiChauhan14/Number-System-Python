st=int(input("enter starting point"))
end=int(input("enter ending point"))
up=int(input("enter updation"))
di=input("enter f or r")
ch=input("enter h or v")
if(di=="f" or di=="r"):
    if(ch=="h" or ch=="v"):
        if di=="f":
            for i in range(a,b+1,c):
                if ch=="h":
                    print(i,end=" ")
                elif (ch=="v"):
                    print(i)
        elif di=="r":
            for i in range(b,a-1,-c):
                   if ch=="h":
                    print(i,end=" ")
                   elif (ch=="v"):
                    print(i)
    else:print("invalid")
else:print("invalid")