# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.
# 

def filter_long_word():
    limit = int(input("Enter How many word you want to enter: "))
    demolist = []
    for i in range(limit):
        demolist.append(input("Enter Word: "))
    print(demolist)
    check_int = int(input("Enter Integer: "))
    newlist = []
    for i in demolist:
        if len(i) > check_int:
            newlist.append(i)
    print(newlist)


filter_long_word()
