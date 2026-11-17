ch = input("enter choice 1. add 2. subtract 3. mult 4. div \n")
print("enter numbers : \n")
a=float(input("enter a \n"))
b=float(input("enter b \n"))
if ch=='1':
    print(f"{a+b}")
elif ch=='2':
    print(f"{a-b}")
elif ch=='3':
    print(f"{a*b}")
elif ch=='4':
    print(f"{a/b}")
else:
    print("invalid choic")