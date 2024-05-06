import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [2, 3, 4, 3]

#criando a "figura" para comportar os gráficos e formar nosso Dashboard
Figura = plt.figure(figsize=(12, 6))
Figura.suptitle('Harry Potter menino maravilhoso')

#adicionando a primeira figura
Figura.add_subplot(331)

plot1 = plt.plot(x, y, label='dados ')
plot1 = plt.title('número de arquivos com dados relevantes')

plt.legend()

#adicionando o segundo plot na figura
Figura.add_subplot(332)
#segundo gráfico teste
cores = ['green','red','blue']
plot2 = plt.bar(x, y, label='número de sugadinhas', color=cores)
plot2 = plt.title('número de cpfs encontrados')

plt.legend()

#adicionando o 3 gráfico
Figura.add_subplot(333)
#terceiro gráfico teste
plot3 = plt.plot(x, y)
plot3 = plt.title('tipo de dado mais encontrado')

plt.legend()

#SEGUNDA LINHA DA FIGURA

#adicionando o 4 gráfico
Figura.add_subplot(334)
#terceiro gráfico teste
fatiax = [3,2,4]
cores = ['green','red','blue']
plot4 = plt.pie(fatiax, colors=cores)
plot4 = plt.title('tipo de dado mais encontrado')

plt.legend()

#adicionando uma terceira figura
Figura.add_subplot(335)
valorx = [5, 7, 3, 9]
valory = [1, 2, 3, 4]
plot4 = plt.scatter(valorx, valory, label='cpf, tamanho peniano')

plt.show()
