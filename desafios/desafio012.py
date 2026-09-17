preco = float(input('Qual é o preço do produto? R$ '))
desconto = preco * 0.05
precofinal = preco - desconto
print('O preço do produto é R$ {:.2f} e com o desconto de 5% o preco final é R$ {:.2f}'.format(preco, precofinal))