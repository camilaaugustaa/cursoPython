#Tupla é uma lista imutável

#lista_vendas = [1000,800,500]
#tupla_vendas = (1000,800,500) #tupla é uma lista imutável e usa parenteses, armazear valores que não devem ser motdificados

#print(lista_vendas[0])
#print(tupla_vendas[0]) 

#lista_vendas [0] = 1200 #lista é mutável
#tupla_vendas [0] = 1200 #tupla não é mutável, não pode ser alterada, vai dar erro!

#tela = (1920, 1080) # largura e altura
#tela = (3090, 1080) # crianod uma nova tupla substtuindo uma tupla antiga, pois tupla nao pode ser alterada

#bonus 1: R$2 POR VENDA FEITA
#bonus 2: 1% DO VALOR DE VENDAS

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas) # R$2 por venda da lista
    bonus2 = 0.01 * sum(lista_vendas) # 1% do valor total de vendas
    return bonus1, bonus2

vendas = [100 ,200, 4890, 1000, 500]

resultado = calcular_bonus(vendas)
print(resultado)

