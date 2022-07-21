import matplotlib.pyplot as plt

x = [1 , 2]
y = [2 , 3]
plt.plot(x, y)
plt.show

#adicionado pontos
x = [1 , 2 , 5]
y = [2 , 3, 7]

#adicionado titulo
plt. title ("grafico usando python")

#adicionando legenda nos eixos
plt.xlabel("eixo X")
plt.ylabel("eixo y")

plt.plot(x, y)
plt.show