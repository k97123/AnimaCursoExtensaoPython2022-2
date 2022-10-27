# comando input( ): quero permitir que o usuário digite algo...
nome = input('Digite o seu nome: ')
#pede a idade para o usuário "Qual a sua idade?"
idade = int(input('Qual a sua idade? '))


#comando de saída..exibir na tela
print('Boa noite, o seu nome é: {}.\n'.format(nome))
#exiba "Sua idade é..."
print('{} sua idade é {} anos.\n'.format(nome,idade))

#e se eu quisesse mostrar o dobro da idade?
dobro = idade * 2
triplo = idade * 3
print("O dobro da sua idade é {} e o triplo é {}.\n".format(dobro,triplo))


#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"

if (idade >= 18):
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir.")
else:
  resto = (18 - idade)
  print("Você é xóven ainda, xóven ainda. Faltam {} anos para você poder ser preso.".format(resto))

#E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)
#Mostre..(..e você também precisa/precisou prestar o serviço militar obrigatório.)

genero = input("Informe o seu gênero M = Masculono ou F = Feminino? ")
if (genero == "M") and (idade >= 18):
  print('e você também precisa/precisou prestar o serviço militar obrigatório.')

