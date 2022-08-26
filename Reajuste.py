salário = float(input('Qual o valor do salário? R$ '))
novo = salário + (salário * 15 / 100)
print ('O salário de R${:.2f} com o aumento de 15% passa a ser R${:.2f}.'.format(salário, novo))