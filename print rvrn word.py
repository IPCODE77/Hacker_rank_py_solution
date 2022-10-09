# print the all even word in a string
a = 'this is a smart phone'
b = a.split(" ")
c = " "
n = -1
for i in b:
    n += 1
    if len(b[n]) % 2 == 0:
        c += b[n]
        c += " "
    else:
        continue

print(c)
