#1
print("1.")
x=int(input("insira um número: "))
if x<0:
    print("x negativo")
else:
    print("x positivo")
#2.
print("2.")
x=int(input("insira lado a"))
y=int(input("insira lado b"))
z=int(input("insira lado c"))

if x==y==z:
    print("equilatero")
elif x==y or x==z or y==z:
    print("isosceles")
else:
    print("escaleno")
#3.
print("3.")
compra=float(input("preço de compra: "))
venda=float(input("preço de venda: "))
lucro=(venda-compra)/compra
print(lucro*100,"%")
if lucro < 0.1:
    print("o lucro foi menor que 10%")
elif lucro > 0.2:
    print("o lucro foi maior  que 20%")
else:
    print("o lucro foi entre 10% e 20%")
#4
print("4.")
fundo=float(input("fundo histórico: "))
topo=float(input("topo histórico: "))
intervalo = topo - fundo
suporte = fundo + 0.3*intervalo
resist = fundo + 0.6*intervalo
print("Suporte: ",suporte)
print("Resistencia: ",resist)
atual=float(input("preço atual: "))
if atual < suporte:
    print("abaixo do suporte")
elif atual < resist:
    print("entre suporte e resistência")
else:
    print("rompeu topo")
#15
print("15.")
lista = ['bbdc4','itub4','petr4','petr4','bbas3','petr4','sanb4','petr4','bpac3','petr4']
count=0
i=0
while count<len(lista):
    if lista[count] == 'petr4':
        i=i+1
        if i == 2: break
    count = count + 1
print('Petrobrás aparece a segunda vez no índice : ',count)
    
#16
print("16.")
Palavras = [['comprar','vender'],['manter','alerta','indicar'],['tendencia','crash','lucro']]
for i in range(0,len(Palavras)):
    print(Palavras[i])
#17
print('17.')
for p in Palavras:
    for x in p:
        print(x)

#18
print('18.')
Lista = [[1,2,-1],[3,-1,4,5],[0,0,1,2,-1],[-1,-1,2,2,-1,2,-1],[3,2,0],[1,1,-1,0,2]]
Lista_nova = []
for p in Lista:
    for x in p:
        Lista_nova.append(x)
print(Lista_nova)
import statistics as st
import numpy as ny
Lista_Array = ny.array(Lista_nova)
print(Lista_Array.sum())
print(Lista_Array.max())
print(Lista_Array.min())
print(st.mean(Lista_Array))
print(st.mode(Lista_Array))
print(st.pstdev(Lista_Array))

#19.
print('19.')
Lista = [['ontem','hoje','amanha'],['sp','rj','mg','ce'],['são paulo','rio','santos','cuiabá']]
Lista_nova = []
for p in Lista:
        for x in p:
            Lista_nova.append(x)
print(Lista_nova)
Lista2 = ['férias','negócios']
for i in range(0,len(Lista2)):
    Lista_nova.append(Lista2[i])
print(Lista_nova)
Lista_nova.sort()
print(Lista_nova)
#20.
print('20.')
Lista=['a','b','c','a','d','f','a','b','b','d','c']
Lista_nova =[]
for i in Lista:
    if i not in Lista_nova:
        Lista_nova.append(i)
        Lista_nova.sort()
print(Lista_nova)
    