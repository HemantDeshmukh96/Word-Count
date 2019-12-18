b=[]
a=input("Enter String :")
b.append(a)
ucount = 0
lcount = 0
scount = 0
for ch in a:
    ch1=ord(ch)
    if ch1>=65 and ch1<=90:
        count=1
        ucount=ucount+count
    if ch1>=97 and ch1<=122:
        count=1
        lcount=lcount+count
    if ch1==32:
        count=1
        scount=scount+count
c=a.split()
for i in c:
    for j in c:
        if i==j:
print(c)
print("Uppercase Total Count :%d"%(ucount))
print("Lowercase Total Count :%d"%(lcount))
print("Space Total Count :%d"%(scount))
print(b)