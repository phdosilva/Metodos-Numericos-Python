from sympy import *

listaDeCoeficientes = {
    1: [1],
    2: [3/2, -1/2],
    3: [23/12, -4/3, 5/12],
    4: [55/24, -59/24, 37/24, -9/24],
    5: [1901/720, -1387/360, 109/30, -637/360, 251/720],
    6: [4277/1440, -2641/480, 4991/720, -3649/720, 959/480, -95/288],
    7: [198721/60480, -18637/2520, 235183/20160, -10754/945, 135713/20160, -5603/2520, 19087/60480],
    8: [16083/4480, -1152169/120960, 242653/13440, -296053/13440, 2102243/120960, -115747/13440, 32863/13440, -5257/17280] 
}

def calcularCoeficientes(resultadoFuncao, coeficientes):
    if(len(resultadoFuncao) != len(coeficientes)):
        print("ERRO: Suas listas possuem tamanhos diferentes.")
        print(len(resultadoFuncao), len(coeficientes))
        print(resultadoFuncao, coeficientes)
        exit(0)
    soma = 0

    resultadoFuncao.reverse()

    for i in range(len(resultadoFuncao)):
        soma += resultadoFuncao[i]*coeficientes[i]
    
    return soma

def AdamsBashforth(f, h, n, pts, k):
    result = pts
    coeficientes = listaDeCoeficientes[k]

    (t, y) = result[len(result)-1]

    for i in range(n): 
        pontos = list(result[len(result)-k:])   
        resultadoFuncao = []
        for (t0, y0) in pontos:
            resultadoFuncao.append( f.subs([ ("t", t0), ("y", y0) ]) )
        y = y + h * calcularCoeficientes(resultadoFuncao = resultadoFuncao, coeficientes = coeficientes)
        t += h
        result.append( (t, y) )

    return result

if __name__ == "__main__":
    t, y = symbols("t y")

    f = 1 - t + 4*y
    h = 0.1
    n = 1
    pts = [(0, 1), (0.1, 1.6089333), (0.2, 2.5050062), (0.3, 3.8294145)]
    k = 4

    print(AdamsBashforth(f = f, h = h, pts = pts, n = n, k = k))