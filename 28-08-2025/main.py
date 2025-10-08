m=int (input("enter your num"))
print(m)

match m:
     case 1:
         print("very bad")
     case 2:
         print("bad")
     case 3:
         print("Average")
     case 4:
         print("bad")
     case 5:
         print("Very bad")
     case _:
         print("INVALID")
        
