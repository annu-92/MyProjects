a=int(input("Enter the 1st side of triangle:"))
b=int(input("Enter the 2nd side of triangle:"))
c=int(input("Enter the 3rd side of triangle:"))
print(a,b,c)
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)
