#1.13 exercicios

import math

print("1.")
#a
print("(a) ", math.pow(4,3) - math.pow(2,2))
#b
print("(b) ", math.sin(2) - math.cos(4.2))
#c
print("(c) ", math.cos(math.sin(3.7)) - math.tan(1.3))
#d
print("(d) ", 26 % 4 )
#e
print("(e) ", math.radians(46.2))
#f
print("(f) ", math.degrees(3.1))

#2

print("2.")

x=3
y=6

#a
print("(a) ",math.exp(x) - math.log(y))
#b
print("(b) ",x*math.pow(y, 2) + y*math.cos(x))
#c
print("(c) ",math.sqrt((x/y) + math.log(x+y) + math.tan(x)))

#3
print("3.")

num = [3,3,4,1,2,1,1,2,3,4,4,1,1,5,2]

#a
print("(a) ",num[2:4])
#b
print("(b) ",num[4:9])
#c
print("(c) ",num[1:])
#d
print("(d) ",num[:])
#e
print("(e) ",num[::3])
#f
print("(f) ",num[-1])
#g
print("(g) ",num[-3:])
#h
print("(h) ",num[:4])
#i
print("(i) ",len(num))
#j
print("(j) ",num.count(1))

#4.
print("4.")
Bolsas = ['dow','ibov','ftse','dax','nasdaq','cac']
#a
print("(a) ",Bolsas[:3])
#b
Bolsas.extend(['hong kong','merval'])
print("(b) ",Bolsas)
#c
print("(c) ",Bolsas.index('cac'))
#d
Bolsas.remove('cac')
print("(d) ",Bolsas)
#e
Bolsas.insert(2, 's&p500')
print("(e) ",Bolsas)

#5
print('5.')
bov = ['petr4','vale3','ggbr4',28.4,31.3,15.76]
f=open('bov.txt', 'w')
f.write('%s, %s, %s, %2.1f, %2.1f, %2.2f' % (bov[0],bov[1],bov[2],bov[3],bov[4],bov[5]))
f.close()
print(bov)

#6
print("6.")
f=open('bov.txt','r')
y=f.read()
print(y)

#7
print("7.")
import numpy as ny
import statistics as st
lista =[2,2,3,3,3,-1,-1,-2,0,0,0,2,4,5,1,2,2,0,0,0,2,1,5,5,7,6,5,0,0]
print("(a) ",sum(lista))
print("(b) ",max(lista))
print("(c) ",min(lista))
print('(d)',st.mean(lista))
print("(e)", st.median(lista))
print('(f) ',st.mode(lista))
print('(g)', st.stdev(lista))
print('(h)', st.pstdev(lista))
print('(i) ',lista.count(0))
print('(j) ',lista.count(5))
lista.sort()
print('(k) ',lista)
lista.sort(reverse=True)
print('(l) ',lista)
#8
print("8.")
import xlrd
import matplotlib.pyplot as fig
print("(a)")
wb=xlrd.open_workbook('planilha.xls')
plan = wb.sheet_by_name('Plan1')
vale=plan.col_values(0)
gerdau=plan.col_values(1)
print("vale:",vale,"\n","gerdau: ",gerdau)
print("(b)")
vale3=ny.array(vale)
ggbr4=ny.array(gerdau)
print("array vale:",vale3)
print("array gerdau: ",ggbr4)
print("(c)")
tempo=ny.arange(0,len(vale3))
fig.subplot(211);fig.plot(tempo,vale3)
fig.subplot(212);fig.plot(tempo,ggbr4)
print("(d)")

def retorno(x):
    retx=(x[1:len(x)]-(x[0:(len(x)-1)]))/(x[0:(len(x)-1)])
    return retx
t=ny.arange(0,27)
fig.subplot(221);fig.plot(tempo,vale3)
fig.subplot(222);fig.plot(tempo,ggbr4)
fig.subplot(223);fig.plot(t,retorno(vale3)*100)
fig.subplot(224);fig.plot(t,retorno(ggbr4)*100)
