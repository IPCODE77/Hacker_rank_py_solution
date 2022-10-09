# upper case half of a string
from operator import ne


a="python"
mid=len(a)//2
# start=-1
# newstr=" "
# for i in a:
#     start+=1
#     if start>=mid:
#         newstr+=i.upper() 
#     else:
#         newstr+=i 

# print(newstr)          
# using the list comparehension and range method

new=''.join([a[i].upper() if i>=mid else a[i] for i in range(len(a))])
print(new)