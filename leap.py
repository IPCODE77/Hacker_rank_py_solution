def is_leap(year):
    
    
    # Write your logic here
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
year = int(input("Enter the year: "))
print(is_leap)

a = "subha is a good boy"
print(a.split())
