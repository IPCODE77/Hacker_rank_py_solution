a='my name is itish'
b=a.split()
# print(type(b))
l=[]
for i in b:
  l.append(i)
# print(" ".join(reversed(l)))  

l.reverse()
# print(l)

s=''
for i in l:
    s+=i
    s+=" "
print(s)    