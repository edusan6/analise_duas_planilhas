import pandas as pd
import openpyxl
import xlrd

#ler os arquivos e salva numa vavialvel
excel_novo = pd.read_excel(r'C:\Users\edusa\OneDrive\Documents\Programção\Python\MATRICULADOS EM 2022.2.xlsx')
excel_antigo = pd.read_excel(r'C:\Users\edusa\OneDrive\Documents\Programção\Python\DISCENTE MATRICULADOS.xls')

#cria novas listas em branco para cada arqruivo
lista_novo = []
lista_antigo = []

#com o for uso o metodo append para adicionar os nomes as listas
for nomes in excel_novo["cpf"]:
    lista_novo.append(nomes)

for nome in excel_antigo["cpf"]:
    lista_antigo.append(nome)


print(len(lista_novo))
print(len(lista_antigo))
#usa metodo set para transforma em conjunto, pq alem de eliminar os dados duplicados, também permite utilizar outros metodos
conjunto_a = set(lista_novo)

#salvo na variavel os diferentes diferentes entre a primeira e segunda lista
inter = conjunto_a.difference(lista_antigo)
print(inter)
