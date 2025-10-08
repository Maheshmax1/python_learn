a=int(input("enter your num"))
b=int(input("enter your num"))

if a>0 and b>0:
    print("Quadrent1")

elif a<0 and b>0:
    print("Quadrent2") 

elif  a<0 and b<0:
    print("Quadrent3")     

elif a>0 and b<0:
    print("Quadrent4")  

else:
    print("Quadrent none")  