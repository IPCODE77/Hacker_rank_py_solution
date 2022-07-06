# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.


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
    i=input(f"enter word {i+1}")
    l1.append(i)

value=long_word(l1,num)
print(value)