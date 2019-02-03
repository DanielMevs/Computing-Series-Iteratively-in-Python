import math
"""
    Daniel Mevs
"""
def asubn(n):
    return(int(math.pow(-1,n)))

def bsubn(x,n):
    x *= 2
    return(str(float('%g'%(math.pow(x,n))))) 
def csubn(x,n):
    n *= 2
    return(str(float('%g'%(math.pow(x,n))))) 

def dsubn(n):
    n *= 2
    return(int(math.factorial(n+1)))


def main():
    
    x = float(input("Please input a number for x: "))

    n_list = [1,2,3,4,5,10,19,20]

    
    print('_'*80)

    
    print("{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}".format("n value","(−1)^n","(2x)^n","(x)^2n", "(2n+1)!"))

    print('_'*80)
        
    n_list = [1,2,3,4,5,10,19,20]

    for n in n_list:
           print("{0:<15d}{1:<15d}{2:<15s}{3:<15s}{4:<15d}".format(n, asubn(n), bsubn(x,n), csubn(x,n), dsubn(n))) # example of string interpolation
           
if __name__ == '__main__':
    main()
    
