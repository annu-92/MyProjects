Eng = int(input("Enter marks of English:"))
GK = int(input("Enter marks of GK:"))
EVS = int(input("Enter marks of EVS:"))
Per = (Eng+GK+EVS)/3
if(Per>=50):
    print("pass")
else:
    print("fail")