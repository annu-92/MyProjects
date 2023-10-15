# print greatest number
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if(a>b):
    print("a is greater than b")
else:
    print("a is smaller then b")
    
#to print consonant or vowel
V= input("Enter alphabet:")
if(V=='A') or (V=="E") or (V=='I') or (V=='O') or (V=='U') or (V=="a") or (V=="e") or (V=="i") or (V=="o") or (V=='u'):
    print("vowel")
else:
    print("consonant")


#print number is even or odd

a = int(input("Enter your number:"))
if(a%2==0):
    print("a is an even number")
else:
    print("a is an odd number")
