def largest_number():
    a=[1,2,12,34,2,1,33]
    max=0
    for i in range (len(a)):
        if(a[i]>max):
            max=a[i]
    return max

def Second_largest():
    a=[1,2,12,34,2,1,33]
    a.sort(reverse=True)
    for nums in a:
        if nums !=a[0]:
            return nums
            
def rotation():
    d=2
    a=[1,2,12,34,2,1,33]
    temp=[0]*d
    for i in range(2):
        temp[i]=a[i]
    key=0
    for j in range(d,len(a)):
        a[j-d]=a[j]
        key+=1
    for k in range(key+1,len(a)):
        a[k]=temp[k-key]
    return a

def zero():
    a=[0,1,2,12,0,34,2,1,33]
    i=0
    for j in range(i,len(a)):
        if a[j]!=0:
            a[i]=a[j]
            i+=1
    for j in range(i,len(a)):
        a[j]=0
    return a
    
        
             
        

def main():
    out=zero()
    print(out)
main()
        