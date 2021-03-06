# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UaeBfR9bc9RTFXd9jIz4L89IEvFFxgOw
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
# %pylab inline

t=df0_0.t

df0_0=pd.read_csv('0.0_0.txt',delimiter=' ')
df0_01=pd.read_csv('0._01.txt',delimiter=' ')
df0_1=pd.read_csv('0._1.txt',delimiter=' ')
df0_2=pd.read_csv('0._2.txt',delimiter=' ')
df0_3=pd.read_csv('0._3.txt',delimiter=' ')
df0_4=pd.read_csv('0._4.txt',delimiter=' ')
df0_5=pd.read_csv('0._5.txt',delimiter=' ')
df0_6=pd.read_csv('0._6.txt',delimiter=' ')
df0_7=pd.read_csv('0._7.txt',delimiter=' ')
df0_8=pd.read_csv('0._8.txt',delimiter=' ')
df0_9=pd.read_csv('0._9.txt',delimiter=' ')

df0_8.euler

plt.plot(t,df0_0.euler,"r")
plt.plot(t,df0_01.euler,"r")
plt.plot(t,df0_1.euler,"r")
plt.plot(t,df0_2.euler,"r")
plt.plot(t,df0_3.euler,"r")
plt.plot(t,df0_4.euler,"r")
plt.plot(t,df0_5.euler,"r")
plt.plot(t,df0_6.euler,"r")
plt.plot(t,df0_7.euler,"r")
plt.plot(t,df0_8.euler,"r")
plt.plot(t,df0_9.euler,"r")
plt.title("r=0 euler-Kutta módszerrel")
plt.xlabel("Idő")
plt.ylabel("Telítettség")
plt.grid()
plt.xlim(0,10)

dfm05_0=pd.read_csv('-0.5_0.txt',delimiter=' ')
dfm05_01=pd.read_csv('-0.5_01.txt',delimiter=' ')
dfm05_1=pd.read_csv('-0.5_1.txt',delimiter=' ')
dfm05_2=pd.read_csv('-0.5_2.txt',delimiter=' ')
dfm05_3=pd.read_csv('-0.5_3.txt',delimiter=' ')
dfm05_4=pd.read_csv('-0.5_4.txt',delimiter=' ')
dfm05_5=pd.read_csv('-0.5_5.txt',delimiter=' ')
dfm05_6=pd.read_csv('-0.5_6.txt',delimiter=' ')
dfm05_7=pd.read_csv('-0.5_7.txt',delimiter=' ')
dfm05_8=pd.read_csv('-0.5_8.txt',delimiter=' ')
dfm05_9=pd.read_csv('-0.5_9.txt',delimiter=' ')

plt.plot(t,dfm05_0.euler,"r")
plt.plot(t,dfm05_1.euler,"r")
plt.plot(t,dfm05_01.euler,"r")
plt.plot(t,dfm05_2.euler,"r")
plt.plot(t,dfm05_3.euler,"r")
plt.plot(t,dfm05_4.euler,"r")
plt.plot(t,dfm05_5.euler,"r")
plt.plot(t,dfm05_6.euler,"r")
plt.plot(t,dfm05_7.euler,"r")
plt.plot(t,dfm05_8.euler,"r")
plt.plot(t,dfm05_9.euler,"r")
plt.title("r=-0.5 euler-Kutta módszerrel")
plt.xlabel("Idő")
plt.ylabel("Telítettség")
plt.grid()
plt.xlim(0,10)

dfm1_0=pd.read_csv('-1._0.txt',delimiter=' ')
dfm1_01=pd.read_csv('-1._01.txt',delimiter=' ')
dfm1_1=pd.read_csv('-1._1.txt',delimiter=' ')
dfm1_2=pd.read_csv('-1._2.txt',delimiter=' ')
dfm1_3=pd.read_csv('-1._3.txt',delimiter=' ')
dfm1_4=pd.read_csv('-1._4.txt',delimiter=' ')
dfm1_5=pd.read_csv('-1._5.txt',delimiter=' ')
dfm1_6=pd.read_csv('-1._6.txt',delimiter=' ')
dfm1_7=pd.read_csv('-1._7.txt',delimiter=' ')
dfm1_8=pd.read_csv('-1._8.txt',delimiter=' ')
dfm1_9=pd.read_csv('-1._9.txt',delimiter=' ')

plt.plot(t,dfm1_0.euler,"r")
plt.plot(t,dfm1_1.euler,"r")
plt.plot(t,dfm1_01.euler,"r")
plt.plot(t,dfm1_2.euler,"r")
plt.plot(t,dfm1_3.euler,"r")
plt.plot(t,dfm1_4.euler,"r")
plt.plot(t,dfm1_5.euler,"r")
plt.plot(t,dfm1_6.euler,"r")
plt.plot(t,dfm1_7.euler,"r")
plt.plot(t,dfm1_8.euler,"r")
plt.plot(t,dfm1_9.euler,"r")
plt.title("r=-1 euler-Kutta módszerrel")
plt.xlabel("Idő")
plt.ylabel("Telítettség")
plt.grid()
plt.xlim(0,10)

df1_0=pd.read_csv('1._0.txt',delimiter=' ')
df1_01=pd.read_csv('1._01.txt',delimiter=' ')
df1_1=pd.read_csv('1._1.txt',delimiter=' ')
df1_2=pd.read_csv('1._2.txt',delimiter=' ')
df1_3=pd.read_csv('1._3.txt',delimiter=' ')
df1_4=pd.read_csv('1._4.txt',delimiter=' ')
df1_5=pd.read_csv('1._5.txt',delimiter=' ')
df1_6=pd.read_csv('1._6.txt',delimiter=' ')
df1_7=pd.read_csv('1._7.txt',delimiter=' ')
df1_8=pd.read_csv('1._8.txt',delimiter=' ')
df1_9=pd.read_csv('1._9.txt',delimiter=' ')

plt.plot(t,df1_0.euler,"r")
plt.plot(t,df1_1.euler,"r")
plt.plot(t,df1_01.euler,"r")
plt.plot(t,df1_2.euler,"r")
plt.plot(t,df1_3.euler,"r")
plt.plot(t,df1_4.euler,"r")
plt.plot(t,df1_5.euler,"r")
plt.plot(t,df1_6.euler,"r")
plt.plot(t,df1_7.euler,"r")
plt.plot(t,df1_8.euler,"r")
plt.plot(t,df1_9.euler,"r")
plt.title("r=1 euler-Kutta módszerrel")
plt.xlabel("Idő")
plt.ylabel("Telítettség")
plt.grid()
plt.xlim(0,10)

df05_0=pd.read_csv('0.5_0.txt',delimiter=' ')
df05_01=pd.read_csv('0.5_01.txt',delimiter=' ')
df05_1=pd.read_csv('0.5_1.txt',delimiter=' ')
df05_2=pd.read_csv('0.5_2.txt',delimiter=' ')
df05_3=pd.read_csv('0.5_3.txt',delimiter=' ')
df05_4=pd.read_csv('0.5_4.txt',delimiter=' ')
df05_5=pd.read_csv('0.5_5.txt',delimiter=' ')
df05_6=pd.read_csv('0.5_6.txt',delimiter=' ')
df05_7=pd.read_csv('0.5_7.txt',delimiter=' ')
df05_8=pd.read_csv('0.5_8.txt',delimiter=' ')
df05_9=pd.read_csv('0.5_9.txt',delimiter=' ')

plt.plot(t,df05_0.euler,"r")
plt.plot(t,df05_1.euler,"r")
plt.plot(t,df05_01.euler,"r")
plt.plot(t,df05_2.euler,"r")
plt.plot(t,df05_3.euler,"r")
plt.plot(t,df05_4.euler,"r")
plt.plot(t,df05_5.euler,"r")
plt.plot(t,df05_6.euler,"r")
plt.plot(t,df05_7.euler,"r")
plt.plot(t,df05_8.euler,"r")
plt.plot(t,df05_9.euler,"r")
plt.title("r=0.5 euler-Kutta módszerrel")
plt.xlabel("Idő")
plt.ylabel("Telítettség")
plt.grid()
plt.xlim(0,10)

def anal(x_0,r,t): 
  return 1/(1+((1/x_0)-1)*np.exp(-r*t))
anals = [anal(x_0/10,0,t) for x_0 in range(1,11,1)]
plt.plot(anals)

anals = [anal(x_0/10,1,t) for x_0 in range(1,11)]
plt.plot(df1_0.runge,"r")
plt.plot(df1_1.runge,"r")
plt.plot(df1_01.runge,"r")
plt.plot(df1_2.runge,"r")
plt.plot(df1_3.runge,"r")
plt.plot(df1_4.runge,"r")
plt.plot(df1_5.runge,"r")
plt.plot(df1_6.runge,"r")
plt.plot(df1_7.runge,"r")
plt.plot(df1_8.runge,"r")
plt.plot(df1_9.runge,"r")
plt.plot(anals,'b')
plt.xlim(0,10)
plt.grid()
plt.title("r=1 runge-kutta módszer összehasonlítása az analitikussal")
plt.xlabel("Idő")
plt.ylabel("Telítettség")

df2=pd.read_csv("outs.txt",delimiter=' ')       
#r1=r2=0.4, alpha=béta=0.4, k1=0.2, k2=0.8, #az egyik faj eltűnik#1
df2m=pd.read_csv("outs_békélés.txt",delimiter=' ') 
#r1=r2=0.4, alpha=béta=0.4, k1=0.7, k2=0.8, #egyensúlyhoz az adatok

plt.plot(df2.t,df2.n1,label="Első faj")
plt.plot(df2.t,df2.n2,label="Második faj")
plt.title("A két állatfaj populációjának telítettsége időben")
plt.xlabel("Idő")
plt.ylabel("Egymáshoz viszonyított populáció")
legend()
grid()

plt.plot(df2.n1,df2.n2)
xlabel("Első faj populációjának telítettsége")
ylabel("Második faj populációjának telítettsége")
grid()

plt.plot(df2m.t,df2m.n1,label="Első faj")
plt.plot(df2m.t,df2m.n2,label="Második faj")
plt.title("A két állatfaj populációjának telítettsége időben")
plt.xlabel("Idő")
plt.ylabel("Egymáshoz viszonyított populáció")
legend()
grid()

plt.plot(df2m.n1,df2m.n2)
xlabel("Első faj populációjának telítettsége")
ylabel("Második faj populációjának telítettsége")
grid()

df3=pd.read_csv("end.txt",delimiter=' ')

t3=df3.t

plt.plot(df3.nr)
plt.plot(df3.nf)



a = 0.34
b = 0.002
c = 0.0025
d = 0.89

h=1
def f(n):
    # In this function I just return both population change in one numpy array
    return np.array([a*n[0]-b*n[1]*n[0], c*n[0]*n[1]-d*n[1]])
n = [250,100]
def rk4(x,*args):
    # Runge kutta solver I guess not need any explanation
    k1 = f(x,*args)
    k2 = f(x+0.5*h*k1,*args)
    k3 = f(x+0.5*h*k2,*args)
    k4 = f(x+k3*h,*args)

    return x + h/6 * (k1 + 2* k2 + 2*k3+k4)

nlist=[n]
for i in range(100):
  n=rk4(n)
  nlist.append(n)

naray=np.array(nlist)
naray[:,0]

plt.plot(naray[:,0],label="nyulak")
plt.plot(naray[:,1],label="rókák")
plt.title("Egyedek száma az idő függvényében")
plt.legend()
plt.xlabel("Idő")
plt.ylabel("Egyedek száma")

plt.plot(naray[:,0],naray[:,1])
plt.title("Lotke-Voltera Fázistér")
plt.xlabel("Nyulak száma")
plt.ylabel("Rókák száma")

