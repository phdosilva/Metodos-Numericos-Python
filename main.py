from metodos.euler import *
from metodos.rungeKutta import *
from metodos.adamsBashforth import *
from metodos.adamsMulton import *
from metodos.formulaInversa import *

arqEntrada = open("entrada.txt", "r")
arqSaida = open("saida.txt", "w")

def start():
    for linha in arqEntrada:
        entrada = linha.split(" ")
        
        metodo = entrada[0]

        print(metodo)

        entrada[len(entrada)-1] = entrada[len(entrada)-1].split("\n")[0]

        if metodo == "euler" or metodo == "euler_inverso" or metodo == "euler_aprimorado" or metodo == "runge_kutta":
            try:
                y0 = entrada[1]
                t0 = entrada[2]
                tamPasso = entrada[3]
                qntPassos = entrada[4]
                funcao = entrada[5]
            except:
                print("ERRO 1: Erro na atribuição de entrada para cada variável\nPor favor, confira se a entrada está correta.")
                exit()

            try:
                y0 = float(y0)
                t0 = float(t0)
                tamPasso = float(tamPasso)
                qntPassos = int(qntPassos)
                funcao = simplify(funcao)
            except:
                print("ERRO 2: Erro ao converter tipo das variáveis\nPor favor, confira se a entrada está correta.")
                exit()

            if metodo == "euler":
                resultado = (Euler(f = funcao, p0 = (t0, y0), h = tamPasso, n = qntPassos))
            elif metodo == "euler_inverso":
                # return EulerInversoPorPrevisao(f = funcao, p0 = (t0, y0), h = tamPasso, n = qntPassos)
                resultado = (EulerInversoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = qntPassos))
            elif metodo == "euler_aprimorado":
                # return EulerAprimoradoPorPrevisao(f = funcao, p0 = (t0, y0), h = tamPasso, n = qntPassos)
                resultado = (EulerAprimoradoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = qntPassos))
            elif metodo == "runge_kutta":
                resultado = (RungeKutta(f = funcao, p0 = (t0, y0), h = tamPasso, n = qntPassos))
        elif metodo == "adam_bashforth_by_euler" or metodo == "adam_bashforth_by_euler_inverso" or metodo == "adam_bashforth_by_euler_aprimorado" or metodo == "adam_bashforth_by_runge_kutta" or metodo == "adam_multon_by_euler" or metodo == "adam_multon_by_euler_inverso" or  metodo == "adam_multon_by_euler_aprimorado" or metodo == "adam_multon_by_runge_kutta" or metodo == "formula_inversa_by_euler" or metodo == "formula_inversa_by_runge_kutta" or metodo == "formula_inversa_by_euler_aprimorado" or metodo == "formula_inversa_by_euler_inverso":
            try:
                y0 = entrada[1]
                t0 = entrada[2]
                tamPasso = entrada[3]
                qntPassos = entrada[4]
                funcao = entrada[5]
                ordem = entrada[6]
            except:
                print("ERRO 1: Erro na atribuição de entrada para cada variável\nPor favor, confira se a entrada está correta.")
                exit()

            try:
                y0 = float(y0)
                t0 = float(t0)
                tamPasso = float(tamPasso)
                qntPassos = int(qntPassos)
                funcao = simplify(funcao)
                ordem = int(ordem)
            except:
                print("ERRO 2: Erro ao converter tipo das variáveis\nPor favor, confira se a entrada está correta.")
                exit()

            # k = ordem - 1
            ordem -= 1

            if metodo == "adam_bashforth_by_euler":
                pts = Euler(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsBashforth(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_bashforth_by_euler_inverso":
                pts = EulerInversoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsBashforth(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_bashforth_by_euler_aprimorado":
                pts = EulerAprimoradoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsBashforth(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_bashforth_by_runge_kutta":
                pts = RungeKutta(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsBashforth(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_multon_by_euler":
                pts = Euler(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsMulton(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_multon_by_euler_inverso":
                pts = EulerInversoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsMulton(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_multon_by_euler_aprimorado":
                pts = EulerAprimoradoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsMulton(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_multon_by_runge_kutta":
                pts = RungeKutta(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (AdamsMulton(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "formula_inversa_by_euler":
                pts = Euler(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (FormulaInversa(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "formula_inversa_by_euler_inverso":
                pts = EulerInversoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (FormulaInversa(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "formula_inversa_by_euler_aprimorado":
                pts = EulerAprimoradoImplicito(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (FormulaInversa(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "formula_inversa_by_runge_kutta":
                pts = RungeKutta(f = funcao, p0 = (t0, y0), h = tamPasso, n = ordem)
                resultado = (FormulaInversa(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
        elif metodo == "adam_bashforth" or metodo == "adam_multon" or metodo == "formula_inversa":
            try:
                y = entrada[1:len(entrada)-5]
                t0 = entrada[len(entrada) - 5]
                tamPasso = entrada[len(entrada) - 4]
                qntPassos = entrada[len(entrada) - 3]
                funcao = entrada[len(entrada) - 2]
                ordem = entrada[len(entrada) - 1]
            except:
                print("ERRO 1: Erro na atribuição de entrada para cada variável\nPor favor, confira se a entrada está correta.")
                exit()

            try:
                y = [float(i) for i in y]
                t0 = float(t0)
                tamPasso = float(tamPasso)
                qntPassos = int(qntPassos)
                funcao = simplify(funcao)
                ordem = int(ordem)
            except:
                print("ERRO 2: Erro ao converter tipo das variáveis\nPor favor, confira se a entrada está correta.")
                exit()

            pts = []
            for i in range(len(y)):
                pts.append((t0, y[i]))
                t0 += tamPasso
        
            ordem -= 1

            if metodo == "adam_bashforth":
                resultado = (AdamsBashforth(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "adam_multon":
                resultado = (AdamsMulton(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
            elif metodo == "formula_inversa":
                resultado = (FormulaInversa(f = funcao, h = tamPasso, n = qntPassos, pts = pts, k = ordem))
        else:
            print("ERRO: Nenhum método selecionado.")

        textoDeSaida = ""

        textoDeSaida += metodo + '\n'
        textoDeSaida += "y( " + str(resultado[0][0]) + " ) = " + str(resultado[0][1]) + "\n"
        textoDeSaida += "h = " + str(tamPasso) + "\n"
        for i in range(len(resultado)):
            textoDeSaida += str(i) + " " + str(resultado[i][1]) + "\n"
        textoDeSaida += "\n"


        arqSaida.write(textoDeSaida)


    #fim for

    return
if __name__ == "__main__":
    start()