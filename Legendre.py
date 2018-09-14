#Deniel Lima Lopez
#14/09/2018
#Polinomio de Legendre

import numpy as np


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
def pnx(n,x):
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

  #Evaluamos el polinomio derivado n veces en x, d(x)
  d = 0
  for i in range(0,len(p)):
    auxp = p[i]*x**i
    d = d + auxp
  
  pn = d/((2**n)*fac(n))
  
  for i in range(0,len(p)):
    p[i] = p[i]/((2**n)*fac(n))

#Imprimimos el polinomio de Legendre
  print (end="Pn(x) = ")
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
    
  return pn


n = int(input("Ingrese n: "))
x = float(input("Ingrese x: "))

pn = pnx(n,x)
print ("\nPn(",x,") = ",pn)

