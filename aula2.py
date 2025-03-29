faturamento = 1000
custo = 600

lucro = faturamento - custo
texto = f"O lucro foi de R${lucro}, e o faturamento foi de R${faturamento}" #f significa formatt que é uma formatação de string
print(texto)

email = "camila_linda@gmail.com"

print(email.lower()) #lower é minúsculo
print(email.strip()) #strip tira os espaços

#tamanho - len vem de length que é comprimento
print(len(email)) 

#posição
posicao = email.find("@")
print(posicao)
 
#pedaços do texto slice= cortar
print(email[12])
print(email[12:20]) #indice é a posição da letra 0 1 2 3 4... o inicio do corte é inclusivo e o final é exclusivo pega o 5 mas nao pega 20
servidor = email[posicao:]
print(servidor)

#trocar um pedaço do texto
novo_email = email.replace("linda", "maravilhosa")
print(novo_email)

nome = "camila augusta"
nome = nome.capitalize()
print(nome)

nome = nome.title()
print(nome)

print(nome.upper())


faturamento = 1_000_000
custo = 600

lucro = faturamento - custo
margem = lucro/faturamento
texto = f"O lucro foi de R${lucro:,.2f}, e o faturamento foi de R${faturamento:,.2f} e a amrgem foi de R${margem:.1%}" #f significa formatt que é uma formatação de string
print(texto)

