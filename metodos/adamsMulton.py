from sympy import *

listaDeCoeficientes = {
    1: [1],
    2: [1/2,1/2],
    3: [5/12, 2/3, -1/12],
    4: [3/8, 19/24, -5/24, 1/24],
    5: [251/720, 323/360, -11/30, 53/360, -19/720],
    6: [95/288, 1427/1440, -133/240, 241/720, -173/1440, 3/160],
    7: [19087/60480, 2713/2520, -15487/20160, 586/945, -6737/20160, 263/2520, -863/60480],
    8: [5257/17280, 139849/12060, -4511/4480, 123133/120960, -88547/120960, 1537/4480, -11351/120960, 275/24192]
}

def AdamsMulton(f, h, n, pts, k):

    result = pts
    coeficientes = listaDeCoeficientes[k]

    (t, y) = result[len(result)-1]

    for i in range(n):
        resultadoBashforth = AdamsBashforth(f = f, h = h, n = 1, pts = result[:], k = k)
        previsao = resultadoBashforth[len(resultadoBashforth)-1]     
        
        pontos = list(result[ len(result)-k+1: ])
        pontos.append(previsao)
        
        resultadoFuncao = []
        for (t0, y0) in pontos:
            resultadoFuncao.append( f.subs([ ("t", t0), ("y", y0) ]) )
            
        y = y + h * calcularCoeficientes(resultadoFuncao = resultadoFuncao, coeficientes = coeficientes)
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

    print(AdamsMulton(f = f, h = h, pts = pts, n = n, k = k))

else:
    from metodos.adamsBashforth import *