import math
def função(x): #f(x) = raiz de x+1
    num = x+1
    função = math.sqrt(num)

    return função

def imparpar(x):
    if(x%2 == 0): #par
        return True
    else: #impar
        return False

    
#n = int(input("insira o numero de intervalos:"))
n = 20
#b = int(input("insira o valor do extremo superior da integral: "))
b = 1
#a = int(input("insira o valor do extremo inferior da integral: "))
a = 0

h = (b - a) /n #(calculo do numero de passos da tabela de intervalo)

dicionario ={"x0": 0} # cria um dicionario com os valores dos intervalos
x = 1
while x < n: # preeenchimento do dicionario
    key = "x" + str(x)
    dicionario[key] = x/20
    x +=1

dicionario["x"+str(n)] = 1

#o calculo de simpson é realizado a cada 3 pontos (0, 2). (2, 4).... (18,  20)

x = 0
P = 0 # valores fx de x pares 
I = 0 # valores fx de x impares 
while x <= n-1:
    if(x==0):
        E = função(dicionario["x0"])
    else:
        key = imparpar(x)
        if(key):
            P += função(dicionario["x"+str(x)])
        else:
    
            I += função(dicionario["x"+str(x)])
    x+=1
E += função(dicionario["x"+str(x)])

resultado = h/3 * (E+ 4*I + 2*P) #algoritmo
print("o valor aproximado da integral da função √x+1, usando o metodo de Simpson, é de: ")
print(round(resultado, 5))


