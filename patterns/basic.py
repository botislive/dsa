def p1():
    n= input("ENTER A NUMBER TO PRINT PATTERN : ")
    for i in range(int(n)):
        for j in range(int(n)):
            print("*", end="")
            
        print("")
    
    
def p2(n):
      for i in range(n):
          for j in range(i+1):
              print("*", end="")
              
          print("")
    

def p3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        print()
    
def p4(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end="")
        print("")
    

def p5(n):
    for i in range(n,-1,-1):
        for j in range(i+1):
            print("*", end="")
            
        print()

def p6(n):
    for i in range(1,n+1):
        for j in range(1,n+1-i+1):
            print(j, end="")
        print()
            
def p7(n):
    for i in range(n,-1,-1):
            print(" "*i, end="")
            print("*"*((2*n+1)-2*i))
            # print(" "*i, end="")
          
def p8(n):
    for i in range(n,-1,-1):
        print(" "*(n-i+1), end="")
        print("*"*(2*i-1))

def p9(n):


    for i in range(1, n + 1):
        if i % 2 == 0:
            # Even rows: start with 0
            print("0 1 " * (i // 2))
        else:
            # Odd rows: start with 1
            print("1 " + "0 1 " * ((i - 1) // 2))

def p10(n):
    for i in range(1,n+1):
        for j in range():
                spaces=2*(n-i)
                print()
                
def p11(n):
    num=1
    for i in range(1,n+1):
        
        for j in range(1,i+1):
            print(num, end=" ")
            num=num+1
        print()      


def p12(n):
    for i in range(1,n+1):
        for j in (chr(65),chr(65+i)):
            print(j, end=" ")
        print()






def main():
    p12(4)

main()