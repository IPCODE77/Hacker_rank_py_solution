def vowel():
    list=['a','e','i','o','u']
    user=input("Enter character : ")
    try:
        if  len(user)!=1:
            raise ValueError()
    except Exception as e:
        print("Program only check 1st character of a word")
    finally:            
        user=user[0:1].lower()
    if user in list:
          return '1st Character is vowel'
    else:
          return '1st character is not a vowel'      
       
result=vowel()
print(result)

