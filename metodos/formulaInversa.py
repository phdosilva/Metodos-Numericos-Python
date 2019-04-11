from sympy import *

listaDeCoeficientes = {# [yn, ..., yn-1,fn+1]
    1: [1, 1],
    2: [4/3, -1/3, 2/3],
    3: [18/11, -9/11, 2/11, 6/11],
    4: [48/25, -36/25, 16/25, -3/25, 12/25],
    5: [300/137, -300/137, 200/137, -75/137, 12/137, 60/137],
    6: [360/147, -450/147, 400/147, -225/147, 72/147, -10/147, 60/147]
}

def FormulaInversa(f, h, n, pts, k):

    result = pts
    coeficientes = listaDeCoeficientes[k]

    (t, y) = result[len(result)-1]

    for i in range(n):
        resultadoBashforth = AdamsBashforth(f = f, h = h, n = 1, pts = result[:], k = k)
        previsao = resultadoBashforth[len(resultadoBashforth)-1]

        tuplasDePontos = list(result[ len(result)-k+1: ])
        pontos = []
        # print(previsao)
        (t0, y0) = previsao
        pontos.append( h * f.subs([ ("t", t0), ("y", y0) ]) )
        for (aux, y) in tuplasDePontos:
            pontos.append(y)
        
        y = calcularCoeficientes(resultadoFuncao = pontos, coeficientes = coeficientes)
        t += h

        result.append( (t, y) )
        
    return result

if __name__ == "__main__":
    from adamsBashforth import * 
    
    t, y = symbols("t y")

    f = 1 - t + 4*y
    h = 0.1
    n = 3
    pts = [(0, 1), (0.1, 1.6089333), (0.2, 2.5050062), (0.3, 3.8294145)]
    k = 4

    print(FormulaInversa(f = f, h = h, pts = pts, n = n, k = k))

else:
    from metodos.adamsBashforth import *