# Algoritmo Runge-Kutta para k = 4

from sympy import *

def RungeKutta(f, p0, h, n):
    t, y = p0
    result = []
    for i in range(n):
        result.append( (t, y) )
        
        k1 = f.subs([("t", t), ("y", y)])
        k2 = f.subs([("t", t + h/2), ("y", y + h/2*k1)])
        k3 = f.subs([("t", t + h/2), ("y", y + h/2*k2)])
        k4 = f.subs([("t", t + h), ("y", y + h*k3)])

        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        t += h

    return result

if __name__ == "__main__":
    t, y = symbols("t y")

    f = 1 - t + 4*y
    h = 0.1
    p0 = (0, 1)
    n = 11

    print(RungeKutta(f = f, h = h, p0 = p0, n = n))