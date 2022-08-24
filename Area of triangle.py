# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# with constructor

# class length:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
# class calculate(length):
#     def __init__(self, a, b, c):
#         super().__init__(a, b, c)
#         s=(self.a+self.b+self.c)/2
#         area=(s*(s-a)*(s-b)*(s-c))**0.5
#         print(area)


# x=calculate(4,5,6)

# using inner function

class triangle:
    def length(self):
        self.a = float(input("Enter 1st length: "))
        self.b = float(input("Enter 2nd length: "))
        self.c = float(input("Enter 3rd length: "))


class calculate(triangle):
    def result(self):
        s = (self.a + self.b + self.c) / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        print(area)


x = calculate()
x.length()
x.result()
