list1=[""]
list2=[]
l=0
c="(),+-=/\\%&"
a="add(a,mul(50.0,5+1))"
print(a)
count=0;
for b in a:
     if b in c:
         list1=list1+[""+b]
         list1=list1+[""]
         
     else:
         l=len(list1)-1
         list1[l]=list1[l]+""+b
for b in list1:
    if len(b.strip())>0:
        list2=list2+[b.strip()]
print(list2)
l=len(list2)
for b in range(len(list2)):
    lis=len(list2[b])
    print(list2[b],end="")
    if lis>0:
        ll=list2[b]
        s=""
        if len(ll)>0:
            s=ll[0]
        if b+1>l:
            if list2[b+1]=="(":
                if (s>="A" or s>="a") and (s>="Z" or s<="z"):
                    print("=keyword")
        elif(s>="A" or s>="a") and (s<="Z" or s<="z"): 
            print("=variable")
        elif(s>="0" and s<="9"):
            if "." in list2[b]:
                print("=float")
            else:
                print("=integer")
        elif s in c:
            print("=operator")
        else:
            print("=error")


