# Neste aquivo estão presentes os métodos de euler, euler inverso e euler aprimorado.
# O Retorno de cada função é um dicionário, que tem como chave o valor de t, e como resultado o valor de y(t)

from sympy import *

def Euler(f, p0, h, n):
    t, y = p0
    result = []
    for i in range(n):
        result.append( (t, y) )
        k1 = f.subs([("t", t), ("y", y)])
        y = y + h*k1
        t += h

    return result

def EulerInversoPorPrevisao(f, p0, h, n):
    t, y = p0
    result = []
    for i in range(n):
        result.append( (t, y) )
        k1 = f.subs([("t", t), ("y", y)])
        k2 = f.subs([("t", t + h), ("y", y + h*k1)])
        y = y + h*k2
        t += h

    return result

def EulerInversoImplicito(f, p0, h, n):
    t, y = p0
    result = []

    for i in range(n):
        result.append( (t, y) )

        fNMaisUm = f.subs([("t", "tNMaisUm"), ("y", "yNMaisUm")])

        yNMaisUm = symbols("yN") + symbols("h") * fNMaisUm

        yNMaisUm = yNMaisUm.subs("tNMaisUm", t + h)
        yNMaisUm = yNMaisUm.subs("h", h)
        yNMaisUm = yNMaisUm.subs("yN", y)
        yNMaisUm = expand(yNMaisUm)

        yNMaisUm = simplify( symbols("yNMaisUm") - yNMaisUm )
        ladoDireito = - yNMaisUm.subs("yNMaisUm", 0)
        yNMaisUm = yNMaisUm + ladoDireito

        ladoDireito = ladoDireito * symbols("yNMaisUm")/yNMaisUm
        yNMaisUm = yNMaisUm * symbols("yNMaisUm")/yNMaisUm

        y = float(ladoDireito)
        t += h

    return result

def EulerAprimoradoPorPrevisao(f, p0, h, n):
    t, y = p0
    result = []
    for i in range(n):
        result.append( (t, y) )
        k1 = f.subs([("t", t), ("y", y)])
        k2 = f.subs([("t", t + h), ("y", y + h*k1)])

        y = y + h/2 * (float(k1) + float(k2))
        t += h

    return result

def EulerAprimoradoImplicito(f, p0, h, n):
    t, y = p0
    result = []
    for i in range(n):
        result.append( (t, y) )

        fN = f.subs([("t", "tN"), ("y", "yN")])
        fNMaisUm = f.subs([("t", "tNMaisUm"), ("y", "yNMaisUm")])
    
        yNMaisUm = symbols("yN") + symbols("h")/2 * (fN + fNMaisUm)

        yNMaisUm = yNMaisUm.subs([("tN", t), ("yN", y), ("h", h), ("tNMaisUm", t + h)])
        yNMaisUm = expand(yNMaisUm)

        yNMaisUm = simplify( symbols("yNMaisUm") - yNMaisUm )
        ladoDireito = - yNMaisUm.subs("yNMaisUm", 0)
        yNMaisUm = yNMaisUm + ladoDireito

        ladoDireito = ladoDireito * symbols("yNMaisUm")/yNMaisUm
        yNMaisUm = yNMaisUm * symbols("yNMaisUm")/yNMaisUm

        y = float(ladoDireito)
        t += h

    return result

if __name__ == "__main__":
    t, y = symbols("t y")

    f = 1 - t + 4*y
    h = 0.01
    p0 = (0, 1)
    n = 11

    print(Euler(f = f, h = h, p0 = p0, n = n))
    print(EulerInversoImplicito(f = f, h = h, p0 = p0, n = n))
    print(EulerAprimoradoPorPrevisao(f = f, h = h, p0 = p0, n = n))
    print(EulerAprimoradoImplicito(f = f, h = h, p0 = p0, n = n))