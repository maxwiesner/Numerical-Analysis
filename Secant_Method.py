import math


def secant_method(f, p_0, p_1, N, e):
    ''' Max Wiesner 
        2/16/21

    Approximates the root of a given function f using two points, 
    p_0 and p_1, iterating using the the secant line method.

    --- Criteria ---
    The given points p_0 and p_1 must intersect the x axis.

    --- Parameters ---
    f   : the function to evaluate 
    p_0 : initial point (first)
    p_1 : initial point (second)
    N   : maximum amount of iterations allowed 
    e   : tolerance, maximum error allowed 

    --- Returns ---
    approximation of the root p within the given tolerance. '''

    i = 2
    f_p0 = f(p_0)
    f_p1 = f(p_1)
    while i <= N:
        p_n = p_1 - f_p1*(p_1 - p_0)/(f_p1 - f_p0)
        print(f'p_{str(i).ljust(2)} = {p_n:8.14f}')

        if abs(p_n - p_1) < e:
            print(f'\np found after {i} iterations.')
            return p_n
        i += 1
        p_0 = p_1
        f_p0 = f_p1
        p_1 = p_n
        f_p1 = f(p_n)
    print(f"\nThe method failed after {N} iterations. ")
    return None


# calling with lambda functions
def f(x): return x**7 - 2*x**2 + 3


secant_method(f, 1, 2, 20, 10e-5)
