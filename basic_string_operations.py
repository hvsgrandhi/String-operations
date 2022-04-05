print("we will get to know about the\n length of the string\n string reversal\n equality check\n palindrome check\n substring check")
str1=input("Enter the first string:")                   
str2=input("Enter the second string:")
print("the length of first string is:",len(str1))
print("the length of first string is:",len(str2))
revstr1=''
revstr2=''
for i in str1:
    revstr1=i+revstr1
for i in str2:
    revstr2=i+revstr2
print("Reverse of ",str1,"is ",revstr1)
print("Reverse of ",str2,"is ",revstr2)
if str1 == str2:
    print("strings are equal.")
else:
    print("strings are unequal.")
if str1==revstr1: 
    print("string 1 is palindrome.")
else:
    print("string 1 is not palindrome")
if str2==revstr2: 
    print("string 2 is palindrome.")
else:
    print("string 2 is not palindrome")
substr = input("enter substring for string 1: ")
if substr in str1:
    print("is a substring",substr)
else:
    print("is not a substring", substr)
substr1 = input("enter substring for string 2: ")
if substr1 in str2:
    print("is a substring",substr1)
else:
    print("is not a substring",substr1)
