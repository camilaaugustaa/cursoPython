faturamento = 1000
custo = 400

print("faturamento", faturamento)
novas_vendas = 1000

faturamento = faturamento + novas_vendas
imposto = 0.15 * faturamento #float
print("imposto", imposto)


lucro= faturamento- custo- imposto


#função
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a)!"

print(saudacao('Camila'))
print(f"O seu faturamento foi de R$ {faturamento} e o seu lucro foi de R$ {lucro} e o seu custo foi de R$ {custo}")

#mod resto da divisão
anos = int (310/12)
meses = 310 % 12
print (f" {anos} anos e {meses} meses") 