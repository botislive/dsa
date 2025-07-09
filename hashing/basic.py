def fun1():
    list1=[1,2,1,1,2,4,3,4,5,5]
    hash=[0]*len(list1)
    for item in list1:
        hash[item]+=1
    return hash

def fun2():
    az=['a','b','a','c','b','b','d','e']
    hash=[0]*len(az)
    for item in az:
        hash[ord(item.upper())-65]+=1
    return hash


def main():
    result=fun2()
    print(result)


    
main()
    
