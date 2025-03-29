#INPUT
faturamento = input("Preencha com o faturamento: ")
faturamento = faturamento.replace("R$", "").replace(",", ".",)
faturamento = float(faturamento)
custo = 600

lucro = faturamento - custo
print("Lucro", lucro)

vendas_dia1 = int (input ("Vendas dia 1: "))
vendas_dias2 = int (input("Vendas dia 2: "))
total_vendas = vendas_dia1 + vendas_dias2
print("Total de vendas:", total_vendas)

#LISTAS

lista_vendas = [100, 5, 1000, 800, 35] 
print(lista_vendas[0])

#tamanho da lista
qtde_vendas =len(lista_vendas)
print(qtde_vendas) 


total_vendas = sum(lista_vendas) #soma dos itens da lista
print(total_vendas)

#max, min, media
print(max(lista_vendas))
print(min(lista_vendas))
print(total_vendas / qtde_vendas)

#encontrar um elemento na lista(posição do elemento)

lista_produtos = ["iphone", "ipad", "macbook", "apple watch", "airpods"]
print("airpods" in lista_produtos) #in é um operador que verifica se um elemento está na lista

posicao = lista_produtos.index("macbook") #index é um método que retorna a posição do elemento
print(posicao)

#editar um item da lista
lista_precos = [5000, 7000, 10000, 3000, 1000]
novo_preco =  lista_precos[1] * 1.1
lista_precos[1] = novo_preco
print(lista_precos)

#remover um item da lista remove e pop
lista_produtos.remove("apple watch") # remove é um método que remove um item da lista pelo nome
print(lista_produtos)

item_removida = lista_produtos.pop(2) # pop é um método que remove um item da lista pela posição
print(lista_produtos)
print(item_removida)

#adicionar um item na lista append
lista_produtos.append("macbook") #append é um método que adiciona um item no final da lista
lista2_produtos = ["air tag", "PC" , "macbook"] #extend é um método que adiciona vários itens no final da lista
lista_produtos.extend(lista2_produtos)
print(lista_produtos)

#inserir um item em uma posiçao especifica da lista insert
lista_produtos.insert(1, "airpod max")
print(lista_produtos) 

#contar quantas vezes um item aparece na lista count
print(lista_produtos.count("macbook"))

#ordenar a lista sort
lista_produtos.sort() #sort é um método que ordena a lista em ordem crescente
print(lista_produtos)