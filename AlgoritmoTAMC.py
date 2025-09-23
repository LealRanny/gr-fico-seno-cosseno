'''Como vimos em sala de aula, as funções
f(x) = A.sen(bx + c) + d;
g(x) = A.cos(bx + c) + d;
onde os valores A (amplitude), b (controle da frequência), c (deslocamento horizontal da função) e 
d (deslocamento vertical da função), podem ser representados no plano cartesiano.

Utilize o Python e as bibliotecas de representação gráfica para construir um algoritmo onde o usuário 
digita os valores de a,b, c e d, além da função trigonométrica, para construir o gráfico da função.
Adicione os nomes dos eixos, a escala e o título do gráfico (figura).'''


import numpy as np
import matplotlib.pyplot as plt

escolha_func = None

while True:
    entrada_user = input("Digite a função de seno ou cosseno: ")

    if entrada_user.lower() == 'seno' or entrada_user.lower() == 'cosseno':
        escolha_func = entrada_user.lower()
        break
    else:
        print("Entrada INVÀLIDA! Digite apenas se a função é seno ou cosseno.")

while True:
    try:
        entrada_user = input("Digite o valor de 'a': ")
        valorA = float(entrada_user)
        break
    except ValueError:
        print("Entrada inválida! Digite novamente.")

while True:
    try:
        entrada_user = input("Digite o valor de 'b': ")
        valorB = float(entrada_user)
        break
    except ValueError:
        print("Entrada inválida! Digite novamente.")

while True:
    try:
        entrada_user = input("Digite o valor de 'c': ")
        valorC = float(entrada_user)
        break
    except ValueError:
        print("Entrada inválida! Digite novamente.")

while True:
    try:
        entrada_user = input("Digite o valor de 'd': ")
        valorD = float(entrada_user)
        break
    except ValueError:
        print("Entrada inválida! Digite novamente.")

#aqui é aonde eu começo a plotar o grafico e a gerar os dados
variavelX = np.linspace(-2*np.pi, 2*np.pi, 1000) #aqui estou criando um array 

#aqui calculo o valor de y
if escolha_func == 'seno':
    variavelY = valorA*np.sin(valorB*variavelX+valorC) + valorD
elif escolha_func == 'cosseno':
    variavelY = valorA*np.cos(valorB*variavelX+valorC) + valorD

plt.plot(variavelX,variavelY)

#parte do gráfico
plt.title(f"Gráfico da função {escolha_func.capitalize()}")
plt.xlabel("Eixo X") #rótulo para eixo x
plt.ylabel("Eixo Y") #rótulo para eixo y
plt.grid(True) #adição de grade

plt.show() #para mostrar o gráfico de fato



