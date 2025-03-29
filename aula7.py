#Funções em Python
# def = Define a função
# def nome_funcao(parametros): 
#variaveis criadas dentro das funções só existem dentro da função criada, chamos de variaveis locais


lista_precos1 = [1500 , 1000, 800, 2000]

def calcular_imposto(lista_valores): #a lista_valores é a lista que vai guardar os valores do imposto_total que receberá o retorno
    imposto_total = 0
    for preco in lista_valores:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.1
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

imposto_lista1  = calcular_imposto(lista_precos1)
print(f"O total de imposto é R${imposto_lista1}")

lista_precos2 = [2000, 3000, 4000, 5000]

imposto_lista2 = calcular_imposto(lista_precos2)
print(f"O total de imposto é R${imposto_lista2}")