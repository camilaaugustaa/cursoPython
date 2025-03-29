#DESCUBRA O SERVIDOR DO EMAIL

nome = "Camila Augusta"
email = "camilaaugustasnt@outlook.com"

posicao = email.find("@")
servidor= email[posicao:]
print(servidor)



#DESCUBRA O PRIMEIRO NOME DO USIARIO

primeiro_nome = nome.split(" ")[0]  #split é dividir o texto
print(primeiro_nome)
#ou
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]


#CRIE UMA MSG PERSONALIZADA DIZENDO "Usuário tal foi cadastrado com sucesso no email tal"

msg = f"O usuário {primeiro_nome} foi cadastrado com sucesso no email {email}. Seja bem-vindo(a)!"
print(msg)