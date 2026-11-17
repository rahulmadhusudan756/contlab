def ctof(c):
    return (9/5)*c+32
def ftoc(f):
    return (f-32)*(5/9)

ch=input("enter 1.ftoc 2.ctof")
if ch=='1':
    f=float(input("enter f"))
    print(f"c={ftoc(f)}")
elif ch=='2':
    c=float(input("enter c"))
    print(f"f={ctof(c)}")
else: 
    print("use properly")