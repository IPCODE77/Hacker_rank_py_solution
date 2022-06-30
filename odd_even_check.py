# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

n=24

if(n%2!=0):
    print("Weird")
elif(n%2==0 and 2<=n<=5):
    print('Not Weird')    
elif(n%2==0 and 6<=n<=20):
    print('Weird')    
elif(n%2==0 and n>=20):
    print("Not Weird")    