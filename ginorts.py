# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
st=list(s)
x=[]
for i in st:
    x.append(ord(i))
x.sort()
m=[]
n=[]
y=[]
z=[]
for i in x:
    if i>=97:
        y.append(chr(i))
    elif 65<=i<=96:
        z.append(chr(i))
    else:
        if(i%2!=0):
            m.append(chr(i))
        else:
            n.append(chr(i))
m=m+n
y=y+z+m
y="".join(y)
print(y)


