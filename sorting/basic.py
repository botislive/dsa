def Selection_Sort():
    a=[4,3,1,5,6,7,2]
    for i in range(0,len(a)-1):
        mini=i
        for j in range(i,len(a)):
            if(a[j]<a[mini]):
                mini=j
        a[i],a[mini]=a[mini],a[i]
    return a


def Bubble_Sort():
    b=[2,4,3,1,45,2,34]
    for i in range(len(b)):
        for j in range(len(b)-i-1):
            if(b[j]>b[j+1]):
                b[j],b[j+1]=b[j+1],b[j]
    return b

def Insertion_Sort():
    c=[2,4,3,1,45,2,34]
    for i in range(1,len(c)):
        for j in range(i,0,-1):
            if(c[j]<c[j-1]):
                c[j],c[j-1]=c[j-1],c[j]
    return c
            
            
            
            
    
            

def main():
    il=Insertion_Sort()
    print(il)
    
    
    
main()
            
            