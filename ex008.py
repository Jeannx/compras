preço=float(input('Valor das compras:R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma=int(input('Escolha uma das opções acima:'))
desconto_5=preço - (preço * 5 / 100)
desconto_10=preço - (preço * 10 /100)
juros=preço + (preço * 20 / 100)
parcela_2x= preço / 2
if forma == 1:
    print('Desconto de 10% conscedido, o produto passa a custar: R${:.2f}'.format(desconto_10))
elif forma == 2:
    print('Desconto de 5% conscedido, o produto passa a custa: R${:.2f}'.format(desconto_5))
elif forma == 3:
    print('O produto continuará custando R${:.2f}, dividido no cartão em 2x de R${:.2f}'.format(preço,parcela_2x))
elif forma == 4:
    parcelas=int(input('Quantidade de parcelas:'))
    parcela_3x= preço / parcelas
    print('Com 20% de juros, produto passará a custar R${:.2f}, dividido no cartão em {}x de R${:.2f}.'.format(juros,parcelas,parcela_3x))
else:
    print('Por favor, escolha uma das opções acima!')   
