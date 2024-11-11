a="add(a,mul(50,5))"
print(a)
for b in a:
     if b=="(" or b==")"  or b==",":
         print(b,end="")
     else:
         print(" ",end="")
print("")

