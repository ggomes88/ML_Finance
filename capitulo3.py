import matplotlib.pyplot as fig
import random
from scipy.stats import norm
import statistics as st
import numpy as np

aleat=[]
for i in range(1000):
    x=random.gauss(0,1)
    aleat.append(x)
    
fig.subplot(211)
fig.plot(aleat,color='black')
fig.xlabel('eixo horizontal')
fig.ylabel('numeros aleatorios entre -1 e 1')

fig.subplot(212)
fig.hist(aleat,bins=20,color='gray', density=True)
fig.xlabel('Classes')
fig.ylabel('frequencia')

xmin,xmax = fig.xlim()
media=st.mean(aleat)
desvio=st.pstdev(aleat)
eixo_x = np.linspace(xmin,xmax,100)
eixo_y = norm.pdf(eixo_x,media,desvio)
fig.plot(eixo_x,eixo_y,color='black')
