a="add(a,mul(50,5))"
print(a)
for b in a:
     if b=="(" or b==")"  or b==",":
         print("\n",b)
     else:
         print(b,end="")
print("")

