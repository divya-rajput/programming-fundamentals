def Patterns(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end='')
        print()

def inv_Pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end='')
        print()

def cone_pattern(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(2*(n-i)-1):
            print("*",end="")
        print()
    
        

#Patterns(5)
#inv_Pattern(5)
cone_pattern(10)