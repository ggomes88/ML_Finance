# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 07:43:02 2021

@author: GRG
"""
#importar libraries
import matplotlib.pyplot as plt
import xlrd
import numpy as ny
from scipy import stats

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
#transformar lista em array para poder calcular    
dados1=ny.array(dados1)
dados2=ny.array(dados2)
beta,beta0,r_value,p_value,std_err=stats.linregress(dados1[1],dados2[1])
yLin=beta*dados1[1]+beta0

plt.plot(dados1[1],yLin,'-k',dados1[1],dados2[1],'ok')
plt.xlabel('IBOV')
plt.ylabel('PCAR3')

print('%10.6f %10.6f %5.2f %10.6f %10.8f' %  (beta,beta0,r_value,p_value,std_err))

## correlacao

cor,pval = stats.pearsonr(dados1[1],dados2[1])
print('%10.6f %10.8f' % (cor,pval))
