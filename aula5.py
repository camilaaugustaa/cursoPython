#Dicionário

lista_produtos = ["ipad", "iphone", "airpod"]
lista_precos = [7000, 5000, 2000]

dic_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000} #chave: valor

#pegar um item

produto = "iphone"
posicao = lista_produtos.index(produto)
preco = lista_precos[posicao]
print(f"O preço do {produto} é R${preco}")

print(dic_produtos["iphone"])

dic_vendas ={"camila": [5000, 1000, 10000], "higor": [2000, 3000, 4000]}
print(dic_vendas["camila"])

#adc um item e editar um item

dic_produtos ["iphone"] = dic_produtos["iphone"] * 1.1
dic_produtos ["macbook"] = 12000
print(dic_produtos)

#remover um item
item_removido = dic_produtos.pop("macbook")
print(dic_produtos)
print(item_removido)

#verificar se existe um item

print("iphone" in dic_produtos)
print("iphone" in dic_produtos.keys()) #verificar se existe a chave
print(5500 in dic_produtos.values()) #verificar se existe o valor

#transformar dicionário em lista

produtos = list(dic_produtos.keys())
print(dic_produtos)
precos = list(dic_produtos.values())
print(precos)

#contagem de itens no dicionário

qtde = len(dic_produtos)
print(qtde)

dic_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000}

produto_buscado = input("Digite o nome do produto: ")
if produto_buscado in dic_produtos:
    print(f"O preço do {produto_buscado} é R${dic_produtos[produto_buscado]}")
else:
    print("Produto não cadastrado, deseja cadastrar?")
    opcao = input("Digite 's' para sim e 'n' para não: ")
    if opcao == "s":
        valor = float(input("Digite o preço do produto: "))
        dic_produtos [produto_buscado] = valor
        
        print("Produto cadastrado com sucesso!")
        print(dic_produtos)
    else:
        print("Produto não cadastrado")
        
        
    