# comando input( ): quero permitir que o usuário digite algo...
nome = input('Digite o seu nome: ')
#pede a idade para o usuário "Qual a sua idade?"
idade = int(input('Qual a sua idade: '))


#comando de saída..exibir na tela
print('Boa noite, o seu nome é: {}.\n'.format(nome))
#exiba "Sua idade é..."
print('{} sua idade é {} anos.\n'.format(nome,idade))

#e se eu quisesse mostrar o dobro da idade?
dobro = idade * 2
triplo = idade * 3
print("O dobro da idade é {} e o triplo é {}.\n".format(dobro,triplo))
