#O(log10N +1)
def bf(n):
    count=0
    while (n>0):
        count=count+1
        n=n//10
    return count  

import math 

#O(1)
def optimal(n):
    return int(math.log10(n)+1)       
  
 
def arms(n):
    temp=n
    power=len(str(temp))
    sum=0
    while n>0:
        last_digit=n%10
        sum=sum+last_digit**power
        n=n//10
    return True if (sum==temp) else False 
 
def div_optimal(n):
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            if(i==n//i):
                print(i) 
            else:
                 print(i,n//i,sep="\n")
            
        
               
def main():
    div_optimal(36)
    
main()