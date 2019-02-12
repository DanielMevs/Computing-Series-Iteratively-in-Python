import math
"""
    Daniel Mevs
    Homework number 4 Extra Credit
"""

def p1():
    x = int(input("Please input a value for x: "))
    print("The value of x is: ", x)
    return x

def p2(x,N):
    if(x == 0):
        return 0
    x= float(x)
    s = 1.0
    tn = 1.0
    for n in range(1, N+1):
        tn /= n
        tn *= x
        s += tn
    print("For E the last term is: ", tn,"\nSum is: ", s,"\nexp(x) is: ", math.exp(x), "\n")
    return s
        
    

def p3(x, N):
    if(x == 0):
        return 0
    x = float(x)
    tn = 1.0
    prev_fact = 1.0
    s= 0.0
    #new_x = -1.0
    new_x = 1*x
    for n in range(1, N + 1):
        tn = new_x/prev_fact
        s += tn
        prev_fact *= (2*n+1)*(2*n)
        new_x *= (-1)*(x*x)

    tn = new_x/prev_fact
    print("For S the last term is: ", tn,"\nSum is: ", s,"\nsin(x) is: ", math.sin(x), "\n")
    return s

def p4(x, N):
    if(x == 0):
        return 0
    tn = 1.0
    prev_fact = 1.0
    s= 0.0
    #new_x = -1.0
    new_x = 1*x
    for n in range(1, N + 1):
        tn = new_x/prev_fact
        s += tn
        prev_fact *= (2*n-1)*(2*n)
        new_x *= (-1)*(x*x)

    tn = new_x/prev_fact
    print("For C the last term is: ", tn,"\nSum is: ", s,"\ncos(x) is: ", math.cos(x), "\n")
    return s


def main():

   
    x = p1()
    n = 86
    print("Using N=", n, "\n")
    #sol = p2(x, n)
    p2(x, n)
    #sol = p3(x, n)
    p3(x, n)
    #sol = p4(x, n)
    p4(x, n)
    
    
                       
##    x = p1()
##    N = 10
##    p2(x, N)
##    p3(x, N)
##    p4(x, N)
   
if __name__ == '__main__':
    main()


