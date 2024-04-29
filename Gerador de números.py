# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 01:01:43 2024

@author: Marcelo Melo
"""
#importa a biblioteca
import random
from tkinter import *


                    
def gerar():
    file = open("numeros_gerados.txt",'w')#abre um arquivo .txt
    
    ddi =int(entrada_ddi.get())
    ddd = int(entrada_ddd.get())
    quantidade = int(entrada_quantidade.get())
    numeros_gerados=[]
    
    #gerador aleatório
    for i in range(0,quantidade):
        n=random.randint(1111, 9999)#gera um número entre 1111 e 9999
        numeros_gerados.append(n)#adiciona o número gerado a lista
        
    #recolhe o número aleatório da lista e imprime o resultado final  
    for j in range(0,quantidade):
        p=random.randint(0,quantidade-1)#pega o resultado de um indice aleatório da lista
        s=random.randint(0,quantidade-1)
        print('+{} {} 9{}-{}'.format(ddi, ddd, numeros_gerados[p], numeros_gerados[s]))
        file.write('+{} {} 9{}-{}\n'.format(ddi, ddd, numeros_gerados[p], numeros_gerados[s]))#escreve o resultado no .txt
        
    file.close()#fecha o arquivo .txt

#GUI
window=Tk()
window.title('Gerador de Números')
window.geometry("300x200+10+10")

label_ddi=Label(window, text='DDI')
label_ddi.place(x=10, y=10)

entrada_ddi=Entry(window, text="ddi", bd=5)
entrada_ddi.place(x=80, y=10)

label_ddd=Label(window, text='DDD')
label_ddd.place(x=10, y=50)

entrada_ddd=Entry(window, text="ddd", bd=5)
entrada_ddd.place(x=80, y=50)

label_quantidade=Label(window, text='Quantidade')
label_quantidade.place(x=10, y=90)

entrada_quantidade=Entry(window, text="quantidade", bd=5)
entrada_quantidade.place(x=80, y=90)

btn_gerar=Button(window, text="Gerar Númerar", command=gerar)
btn_gerar.place(x=100, y=150)

window.mainloop()

