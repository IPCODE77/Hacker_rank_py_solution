# from functools import reduce
# l = [1,2,3,4]
# val = reduce(lambda a,b: a+b,l)
# print(val)
# def myreduce(add,list_1):
#     return a
# def add(a,b):
#     return a+b
# list_1=[10,15,25,40,10]
# a=list_1[0]
# for i in range(1,len(list_1)):
#     b=list_1[i]
#     a=add(a,b)
# print(myreduce(add,list_1))

# l =[10,20,10,40,50]
# print(range(1,len(l)))

# def myfilter(is_even,list_2):
#     return is_even()
# list_2=[34,56,25,67,89,90,103,408]
# list_3=[]
# def is_even():
#     for i in list_2:
#         if i%2==0:
#             list_3.append(i)
#     print(list_3)
# myfilter(is_even,list_2)
# user=(input("Enter: "))
# for i in reversed(range(len(user))):
#             print(user[i],end="")
# if __name__ == '__main__':
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
        
# a = list(score)    
# print(a.sort())
# lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']
# nd = [20,40,30,50,90,10]
# a =sorted(list(set([lst,nd])))
# prin
# l1 = []
# scores = set()
# lowest = []
# for i in range(int(input())):
#         name = input()
#         score = float(input())
#         l1.append([name,score])
#         scores.add(score)
# # print(l1)
# lowest = sorted(scores)[1]
# # print(scores)

# for name,score in l1:
#     if score== lowest:
#         lowest.append(name)
# for name in sorted(lowest):
#     print(name,end="")
# a = {1,6,4,7,4,8}
# b =sorted(a)
# print(type(b)) #
def long_word(list,num):
        l2=[]
        for i in list:
            if(len(i)>num):
                l2.append(i)

        return l2

user=int(input("Enter how many words"))
num=int(input("Enter integer you want to check"))
l1=[]

for i in range(user):
    i=input(f"enter word {i}")
    l1.append(i)

value=long_word(l1,num)
print(value)