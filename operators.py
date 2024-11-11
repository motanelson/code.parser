list1=[""]
l=0
c="(),+-=/\\%"
a="add(a,mul(50,5+1))"
print(a)
count=0;
for b in a:
     if b in c:
         list1=list1+[""+b]
         list1=list1+[""]
         
     else:
         l=len(list1)-1
         list1[l]=list1[l]+""+b
l=len(list1)-1
if list1[l].strip()=="":
    list1=list1[:l-2] 
print(list1)

