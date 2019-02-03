import math
"""
    Daniel Mevs
    Homework number 3
"""

def main():
    
    x = float(input("Please input a number for x: "))

    asubn = int(1)
    bsubn = float(1)
    csubn = float(1)
    dsubn = int(1)

    print('_'*80)

    print("{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}".format("n value","(−1)^n","(2x)^n","(x)^2n", "(2n+1)!"))

    print('_'*80)
        
    n_list = [1,2,3,4,5,10,19,20]
    
    N = sorted(n_list)[len(n_list)-1]
    
    for n in range(1, N+1):
        asubn *= -1# asubn *= -1 same as asubn = asubn * -1
        bsubn = 2 * (x * bsubn)
        csubn = (x*x) * csubn
        dsubn = dsubn * (2*n + 1) * 2*n

        if n in n_list:
            print("{0:<15d}{1:<15d}{2:<15s}{3:<15s}{4:<15d}".format(n, asubn, str('%g'% bsubn), str('%g'%csubn), dsubn))


if __name__ == '__main__':
    main()
    
