def sumofnumber(n):
    if n<1:
        return n
    else:
        return n+sumofnumber(n-1)
print(sumofnumber(int(input())))            