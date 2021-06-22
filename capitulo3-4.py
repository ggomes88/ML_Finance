# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 08:13:40 2021

@author: GRG
"""

#importar libraries
import matplotlib.pyplot as fig
import xlrd
import numpy as ny
from scipy import stats
import statistics as st

#abrix xls
wb=xlrd.open_workbook('BVSP.xls')
plan1=wb.sheet_by_name('BVSP')

wb2=xlrd.open_workbook('PCAR3.SA.xls')
plan2=wb2.sheet_by_name('PCAR3.SA')

#numero de linhas e colunas
lin1=plan1.nrows
col1=plan1.ncols

lin2=plan2.nrows
col2=plan2.ncols

#criar listas vazias
dados1=[]
dados2=[]

#iterar para apendar valores das colunas nas listas
for i in range(col1):
    coluna1=plan1.col_values(i)
    coluna2=plan2.col_values(i)
    dados1.append(coluna1)
    dados2.append(coluna2)
    
dados1=ny.array(dados1)
dados2=ny.array(dados2)    
retorno1=(dados1[1,1:lin1]-dados1[1,0:lin1-1])/dados1[1,0:lin1-1]
retorno2=(dados2[1,1:lin2]-dados2[1,0:lin2-1])/dados2[1,0:lin2-1]

print(stats.ttest_ind(retorno1,retorno2))

fig.subplot(311)
fig.plot(retorno1, '-k')
fig.subplot(312)
fig.plot(retorno2, '-k')
fig.subplot(313)
ax=fig.subplot(313)
ax.boxplot([retorno1,retorno2],showfliers=False)

print(stats.ttest_ind(retorno1,retorno2))
print(st.mean(retorno1))
print(st.mean(retorno2))
