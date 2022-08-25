# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

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
            newlist.append(len(i))
    print(newlist)


filter_long_word()
