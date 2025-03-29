for i in range(10): # range 
    print("Camila é linda e inteligente pra caralho.")
    print(i)
    
    lista_precos = [1500, 1000, 800, 2000]
    #taxa_imposto = 0.1
    
    #for preco in lista_precos:
      #  imposto = preco * taxa_imposto
       # print (f"O preço do produto é R${preco} e o imposto é R${imposto}")
       
#Exemplos
#produdos de até 1000 pagam 10%
#produtos acima de 1000 15%

#for preco in lista_precos:
 #   if preco > 1000:
 #       taxa=  0.15
  #  else:
 #       taxa = 0.1
  #  imposto = preco * taxa
   # print(f"Preço do produto é R${preco} e o imposto é R${imposto}")
   
   
   
total_imposto = 0

for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = preco * taxa
    
    total_imposto = total_imposto + imposto 
    
    print(f"Preço do produto é R${preco} e o imposto é R${imposto}")
    print(f"Total de imposto é R${total_imposto}")
    
#dicionarios {} um dicioonario percorre as chaves do dicionario nao os itens

# calculo percentual de crescimento
# 1600/1500 -1 -> quats % eu cresci de um ano para outro

vendas_23 = {"jan": 15000, "fev": 10000, "mar": 5000}
vendas_24 = {"jan": 16000, "fev": 11000, "mar": 5100}

for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1
    print(f"No mês de {mes} o crescimento foi de {crescimento:.1%}")
    