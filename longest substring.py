# This program tells which have max sublength !
str1=input("Enter the string:")
word=str1.split()
maxlength=0
maxword=""
for i in word:
    x = len(i)
    if x>maxlength and i.isalpha()==True:
        print(i)
        maxlength=x
        maxword=i
    print("Substring with maximum length is :",maxword)
