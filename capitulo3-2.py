import matplotlib.pyplot as fig
import random
from scipy.stats import norm
import statistics as st
import numpy as ny
import csv
import xlrd
import scipy.stats as sci

wb=xlrd.open_workbook('BVSP.xls')
plan = wb.sheet_by_name('BVSP')
lin=plan.nrows
col=plan.ncols
dados=[]

for i in range(col):
    coluna = plan.col_values(i)
    dados.append(coluna)
    
dias=ny.arange(0,lin)
dados=ny.array(dados)
retorno=(dados[1,1:lin]-dados[1,0:lin-1])/dados[1,0:lin-1]

fig.subplot(221)
fig.plot(dias,dados[1])
fig.xlabel('dias')
fig.ylabel('pontos')
fig.title('ibov diario')

fig.subplot(222)
fig.plot(dias[1:],retorno)
fig.xlabel('dias')
fig.ylabel('retorno diario')

fig.subplot(223)
fig.hist(retorno,bins=20,density=True)
fig.xlabel('classes')
fig.ylabel('frequencia')
xmin,xmax=fig.xlim()
media=st.mean(retorno)
desvio=st.pstdev(retorno)
eixo_x=ny.linspace(xmin,xmax,100)
eixo_y=norm.pdf(eixo_x,media,desvio)
fig.plot(eixo_x,eixo_y)

fig.subplot(224)
sci.probplot(retorno, dist='norm', plot=fig)
fig.title('QQ-plot Ibovespa')
