
list=[]
def filter_long_words(list,n) :
    a = [i for i in list if len(i)>n]
    print(a)
user = int(input("Enter the number of words you want check : "))
n = int(input("Enter the length of word you want to check: "))
for i in range(user):
    i = input(f"Enter the {i+1} word: ")
    list.append(i)
    
filter_long_words()


