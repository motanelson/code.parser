list1=[""]
list2=[]
list3=[]
l=0
c="(),+-=/\\%&\""
a='print("%i",add(a,mul(50.0,5+1)))'
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
t=False
starts=False
sstarts=False
for b in range(len(list2)):
    lis=len(list2[b])
    print(list2[b],end="")
    if lis>0:
        ll=list2[b]
        s=""
        if len(ll)>0:
            s=ll[0]
        
        if b+1<l:
            if list2[b+1]=="(":
                if (s>="A" or s>="a") and (s<="Z" or s<="z"):
                    print("=keyword")
                    t=True
        if starts:
            if s=='\"':
                sstarts=True
                print("=string")

        if not(t):
             if not(starts): 
                if(s>="A" or s>="a") and (s<="Z" or s<="z"): 
                    print("=variable")
                elif(s>="0" and s<="9"):
                    if "." in list2[b]:
                        print("=float")
                    else:
                        print("=integer")
                elif s=="\"":
                    
                    starts=not(starts)
                elif s in c:
                    list3=list3+[b]
                    print("=operator")
                else:
                    print("=error")
        if s=="\"" and sstarts:
            starts=not(starts)
        t=False
counter=0
counter2=0
counter3=0
counter4=0
counter5=0
vars0=0
print("----------------------------------------")
counter=0
ttrue=True
for b in range(len(list3)):
    
    if list2[list3[b]]==")":
       
        
        counter2=b
        counter3=b
        counter4=0
        if 0==0:
            counter03=list3[b]
            counter4=0
            while(counter03>-1):
                 if (list2[counter03]=="(" or counter03==0) :
                     
                     if 0==0:
                         tt="var"+str(vars0+counter)        
                         print(tt+"=",end="")
                         for counter5 in range(counter03-1,list3[b]+1):
                             print(list2[counter5],end="")
                             if counter5==counter03-1:
                                 list2[counter5]=tt
                             else:
                                 list2[counter5]=""
                             counter03=-1
                             
                         print(";")
                     
                     counter4=counter4+1
                 counter03=counter03-1
        counter=counter+1