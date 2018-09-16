#Daniel Lima Lopez
#16/09/2018
#Polinomio de Legendre

import numpy as np

#Funcion f(x)

def f(x):
  return x**3 + 2*x**2

#Funcion para calcular pesos
def wi(d,x):
  w = 2/((1-x**2)*d**2)
  return w

#Funcion para evaluar en x
def evaluar(v,x):
  d = 0.0
  for i in range(0,len(v)):
    auxp = v[i]*(x**i)
    d = d + auxp
  
  return d

#Imprimir el polinomio
def imprimir(p):
  s = len(p) - 1
  for g in range(0,len(p)):
    if p[s] != 0:
      if g == 0:
        print (p[s], end="x^")
        print (s, end="")       
      else:
        if p[s] > 0:
          print (end=" + ")
          print (p[s], end="x^") 
          print (s, end="")
        else:
          print (end=" ")
          print (p[s], end="x^") 
          print (s, end="")      
    s = s - 1


#Calcular factorial
def fac(x):
  aux = 1
  
  if x > 1:
    for j in range(1,x+1):
      aux = aux*j
    
  return aux   


#Llenar un vector de ceros en cada espacio  
def vaciar(p,n):
  for i in range(0,n):
    p[i] = 0.0
  return p


#Derivar un polinomio y reacomodarlo en el mismo vector
def derivar(p,c):
  aux = np.arange(0.0,c-1,1.0)
  aux = vaciar(aux,c-1)
  
  for i in range(0,c):
    p[i] = i*p[i] 
    if i > 0:
      aux[i-1] = p[i]
   
  return aux


#Calcular Pn(x)
def pnx(n):
  p = np.arange(0.0,float(2*n+1),1.0)
  p = vaciar(p,2*n+1)

#Desarrollamos el polinomio (x^2-1)^n
  aux = 0
  for k in range(0,n+1):
    p[aux] = (fac(n)/(fac(k)*fac(n-k)))*((-1)**(n-k))
    aux = aux + 2
  
  c = 2*n+1  
  for i in range(0,n):
    p = derivar(p,c)
    c = c - 1

#Calculamos los coeficientes de polinomio de Legendre  
  for i in range(0,len(p)):
    p[i] = p[i]/((2**n)*fac(n))
  return p



n = int(input("Ingrese n: "))
#x = float(input("Ingrese x: "))

#Polinomio de Legendre
p = pnx(n)

#Polinomio de Legendre derivado
p = derivar(p,len(p))
#imprimir(p)
#print ("\n")


a = float(input("Ingrese el indice inferior de la integral: "))
b = float(input("Ingrese el indice superior de la integral: "))

xi = np.arange(0.0,float(n))
xi = vaciar(xi,n)

for i in range(0,n):
  print ("Ingrese x",i+1,": ")
  xi[i] = float(input())

r=1.0
auxs = 0
for i in range(0,n):
  r = wi(evaluar(p,xi[i]),xi[i])*f((b-a)*xi[i]/2+(a+b)/2)
  auxs = auxs + r

integral = (b-a)*auxs/2

print ("EL resultado es: ",integral)



