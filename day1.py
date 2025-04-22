'''******************************************************'''
#1.3D Prime Number
'''def is_prime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True
def sum_dig(a):
    x=sum([int(i)for i in str(a)])
    return x
def tot_dig(a):
    return len(str(a))
'''

'''**************************************************************'''
#Prime Factorization
'''def prime(n):
    if n<1:
        return
    i=2
    while(n%i!=0):
        i+=1
    print(i)
    prime(n//i)
            
n = int(input("Enter a number: "))
prime(n)'''

'''**************************************************************'''
'''Input value Enter a number: aabbaaakc
a2b2a3k1c1'''
a=input("Enter a number: ")
b=""
n=1
for i in range(len(a)):
    if (i+1 < len(a) and a[i]==a[i+1]):
        n=n+1
    else:
        b=b+a[i]+str(n)
        n=1
print(b)