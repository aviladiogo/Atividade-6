import math
#n = int(input("insira o numero de intervalos:"))
n = 20

#b = int(input("insira o valor do extremo superior da integral: "))
b = 1

#a = int(input("insira o valor do extremo inferior da integral: "))
a = 0

h = (b - a) /n #(calculo do numero de passos da tabela de intervalo)

x = 0
SomatorioTotal = 0
SomatorioParcial = 0
#função = raiz de x+1 = math.sqrt(x+1)
while x <= 1.05: #nosso F(x)
    fx = math.sqrt(x+1)
    if(x == 0):
        SomatorioTotal += fx #(pega o valor manimo da função)
    elif(int(x) == 1):
        SomatorioTotal += fx #(pega o valor maximo da função)
    else:
        SomatorioParcial += fx #(valores do meio da tabela)
    x += h

SomatorioTotal += 2*SomatorioParcial #(f(x0)+ 2*f(x1+...+xq)+ f(x1))
Resultado = (h/2) * SomatorioTotal
print("o valor aproximado da integral da função √x+1, usando o metodo de trapezio, é de: ")
print(round(Resultado,5))