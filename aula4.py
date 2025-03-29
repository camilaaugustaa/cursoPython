#condições
faturamento = 200
custo = 600

lucro = faturamento - custo

if lucro >= 0:
    print("Lucro de R$", lucro)
    print("Deu lucro")
else:
    print("Prejuízo de R$", lucro)
    print("Deu prejuízo")
    
print("Fim do programa")

#exemplo 1

produtos = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite o nome do produto: ")

if novo_produto in produtos:
    print("Produto já existente.")
else:
    print(f"Produto {novo_produto} adicionado com sucesso!")
    produtos.append(novo_produto)
    
print(produtos)

#exemplo 2

#vendas_camila =[5000, 1000, 8000, 5000]
#vendas_camila = sum(vendas_camila)
vendedor = input("Digite o nome do vendedor: ")
vendas_camila = int(input(f"Olá {vendedor}! Digite o valor total de suas vendas: "))

if vendas_camila > 15000:
    print("Parabéns, você ganhou um bônus de R$ 500,00")
elif vendas_camila >= 5000:
    print("Parabéns, você ganhou um bônus de R$ 100,00")
else:
    print("Infelizmente você não ganhou um bônus")
    
    
#exemplo 3

vendar_empresa = 200_000
meta_empresa = 100_000

if vendas_camila >=15000 and vendar_empresa >= meta_empresa:
    print("Parabéns, você ganhou um bônus de R$ 500,00")
elif vendas_camila >=5000 and vendar_empresa >= meta_empresa:
    print("Parabéns, você ganhou um bônus de R$ 100,00")
else:
    print("Infelizmente você não ganhou um bônus")