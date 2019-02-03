import math

def p1():
    x = float(input("Please input  a value for x: "))
    print(x)
    return x

def p2(x,N):
    s=0
    for n in range(N+1):
        fact = 1
        for i in range(1,n+1):
            fact*=i
        s+=(x**n)/fact
    print("For E the last term is: ", (x**N)/fact,"\nSum is: ", s)

def p3(x, N):
    s= 0.0 #running sum
    for n in range(N+1):
        fact=1
        for i in range(1,(2*n+2)):
            fact*=i
        t = (((-1)**n)*(x**(2*n+1)))/fact
        s+=t
    print("For S the last term is: ", t,"\nSum is: ", s)

def p4(x, N):
    s= 0.0 #running sum
    for n in range(N+1):
        fact=1
        for i in range(1,(2*n)):
            fact*=i
        t = (((-1)**n)*(x**(2*n)))/fact
        s+=t
    print("For C the last term is: ", t,"\nSum is: ", s)

                
import math
"""
    Daniel Mevs
    Homework number 3
"""
def main():
                       
    x = p1()
    N = 10
    p2(x, N)
    p3(x, N)
    p4(x, N)
   
if __name__ == '__main__':
    main()
