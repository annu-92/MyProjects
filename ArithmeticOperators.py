#addition of two number by taking input from user

A = int(input("Enter first number:"))
B = int(input("Enter second number:"))
c = A+B
print(c)

#distance b/w 2 points

x1=int(input("x coordinate of 1st point:"))
y1=int(input("y coordinate of 1st point:"))
x2=int(input("x coordinate of 2nd point:"))
y2=int(input("y coordinate of 2nd point:"))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
print("Distnce between two points is",distance)

#convert celsius to farenheit

C=int(input("Enter degree celsius:"))
F=(C*9/5)+32
print(F)


#print area of circle

r=int(input("Enter the radius of the circle:"))        #r=radius
pi=3.14
A=pi*r*r     #A=area of circle
print(A)
C=2*pi*r
print(C)

#area of triangle using Herone's formula

a=int(input("Enter the 1st side of triangle:"))
b=int(input("Enter the 2nd side of triangle:"))
c=int(input("Enter the 3rd side of triangle:"))
print(a,b,c)
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)
