# python program for greatest of 3 number using python

def greatstnumber(a,b,c):
  if a>b and a>c:
    print(f"{a} is greater")
  if b>a and b>c:
    print(f"{b} is greater")  
  else:
    print(f"{c} is greater")  

a=float(input())
b=float(input())
c=float(input())
greatstnumber(a,b,c)    