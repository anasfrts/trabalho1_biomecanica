import matplotlib.pyplot as plt
import numpy as np

print("--interseção de duas retas--")

#camera 1
print("Digite os valores da camera 1")
xc1 = float(input("Por favor, insira o valor de x da camera 1: "))
yc1 = float(input("Por favor, Insira o valor de y da camera 1: "))

#projecao 1
print("Digite os valores da projecao da camera 1")
xp1 = float(input("Por favor, insira o valor de x da projecao da camera 1: "))
yp1 = float(input("Por favor, Insira o valor de y da projecao da camera 1: "))

#camera 2
print("Digite os valores da camera 2")
xc2 = float(input("Por favor, insira o valor de x da camera 2: "))
yc2 = float(input("Por favor, insira o valor de y da camera 2: "))


#projecao 2
print("Digite os valores da projecao da camera 2")
xp2 = float(input("Por favor, insira o valor de x da projecao da camera 2: "))
yp2 = float(input("Por favor, insira o valor de y da projecao da camera 2: "))


#coeficiente angular das retas
mr1 = (yp1 - yc1) / (xp1 - xc1) 
mr2 = (yp2 - yc2) / (xp2 - xc2)

#coeficiente linear das restas
br1 = -1 * (mr1 * xc1 - yc1) 
br2 = -1 * (mr2 * xc2 - yc2) 

#cruzamentos
xi = (-(mr2*xc2) + yc2 + (mr1*xc1) - yc1) / (mr1 - mr2) #x do cruzamento
yi = (mr1*xi)  - (mr1*xc1) + yc1 #y do cruzamento


print("Valor do coeficinete angular da reta 1 =", mr1)
print("Valor do coeficiente angular da reta 2=", mr2)
print("valor do coeficiente linear da reta 1=",br1)
print("Valor do coeficiente linear da reta 2=", br2)
print("Valor de x do cruzamento =", xi)
print("Valor de y do cruzamento =", yi)

#grafico
x1 = np.linspace(0,3,100)
y1 = mr1*x1 +br1

x2 = np.linspace(0,3,100)
y2 = mr2*x2 +br2

plt.plot(x1,y1) 
plt.plot(x2,y2)
plt.scatter(xi,yi, color = 'blue') #objeto no plano 
plt.scatter(xc1,yc1, color = 'red') #camera 1 no plano 
plt.scatter(xc2,yc2, color = 'pink') #camera 2 no plano

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title("Cruzamento de retas")
plt.savefig('grafico.png')
