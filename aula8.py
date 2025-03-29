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
bonus1, bonus2 = calcular_bonus(vendas) #Só vai funcionar se a função me devolve dois valores como resposta
#unpacking da tupla, atribuindo os valores retornados da função calcular_bonus para as variaveis bonus1 e bonus2
print(bonus1)
print(bonus2)



#bonus 1: R$2 POR VENDA FEITA
#bonus 2: 1% DO VALOR DE VENDAS

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas) # R$2 por venda da lista
    bonus2 = 0.01 * sum(lista_vendas) # 1% do valor total de vendas
    return bonus1, bonus2

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

#bonus de cada funcionario
# total de bonus 1 pago aos funcionarios
# total de bonus 2 pago aos funcionarios

total_bonus1 = 0
total_bonus2 = 0
for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f"Vendedor {vendedor}. Bonus 1: {bonus1}. Bonus 2: {bonus2}.")
    total_bonus1 = total_bonus1 + bonus1
    total_bonus2 = total_bonus2 + bonus2
    
print("Total Bonus 1:", total_bonus1)
print("Total Bonus 2:", total_bonus2)
print("Total Bonus geral:", total_bonus1)

    