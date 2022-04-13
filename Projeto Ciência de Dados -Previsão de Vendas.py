import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

#Importar a base de vendas 
base = pd.read_excel("Investimento x Vendas.xlsx")

#Exibindo as 5 primeiras linhas 
base.head()

#Visualizando de forma gráfica essas informaçõe
plt.scatter(base["Investimento em marketing"],base["Venda Qtd"]
plt.show()

#Traçando uma reta 
plt.scatter(base["Investimento em marketing"],base["Venda Qtd"])
x0 = base["Investiment em marketing"][0]
y0 = base["Venda Qtd"][0]
x1 = base["Investimento em marketing"][6]
y1 = base["Venda Qtd"][6]
plt.plot([x0,x1],[y0,y1],"r")
plt.show()

#Usando a equação reta para determinar a venda 
 def 
