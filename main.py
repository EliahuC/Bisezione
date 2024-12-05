import sys
import os
import tempfile
import matplotlib.pyplot as plt
import numpy as np
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
 
#creazione delle variabili dall'utente
print( "assegna i valori:")
a = int(input( "Inserisci a: "))
b = int(input("Inserisci b: "))
c = int(input("Inserisci c: "))
d = int(input("Inserisci d: "))

#creazione dell'intervallo dall'utente
v=0
while(v==0) :
 xpos = int(input( "intervallo [a;b] a =  "))
 xneg = int(input("intervallo [a;b] b =  "))
 #controllo parametri 
 if xpos>=0 and xneg<0: 
   v=1 
 else:
   v=0 
   print("i valori non sono validi")
 



#definizione funzione di riferimento
def f(x): return a*x**3+b*x**2+c*x+d

#formula bisezione  
xmedio = (xpos+xneg)/2
ypos = f(xpos)
yneg = f(xneg)
ymedio = f(xmedio)

#ciclo for per determinare risultato:teorema zeri 
for i in range(1000):
   #valore medio positivo
   if ymedio * yneg < 0:
     xpos = xmedio
     xmedio = (xpos + xneg)/2
     ymedio = f(xmedio)
     ypos = f(xpos)
   #valore medio negatico 
   elif ymedio * ypos < 0:
     xneg = xmedio
     xmedio = (xpos + xneg)/2
     ymedio = f(xmedio)
     yneg = f(xneg)
   #valore medio nullo  
   elif ymedio == 0:
     print("P = ", xmedio)
     break
if ymedio != 0:
	   print("P tende a ", xmedio)

 
t = abs(xmedio) + 5 
xpoints = np.linspace(-t, t, 100)
ypoints = f(xpoints)
 
#rappresentazione di titolo x=0 e y=0
plt.title("Metodo di bisezione") 
plt.xlabel("asse x ")
plt.ylabel("asse y") 
plt.plot(xpoints, ypoints)
plt.scatter(xmedio, ymedio)
plt.axhline(y=0)
plt.axvline(x=0)


#rappresentazione legenda e grafico
plt.legend(loc="lower right")
plt.show()
plt.savefig(sys.stdout.buffer)