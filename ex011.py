#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
#para pinta-lá, sabendo que cada litro de tinta pinta um área de 2m².

print('Seja bem-vindo ao nosso sistema!\n')
# Exibe uma mensagem de boas-vindas ao usuário.

print('Descubra a quantidade necessária de tinta para pintar sua \n'
      'parede nos fornecendo as medidas.\n')
# Informa ao usuário sobre a finalidade do programa, que é calcular a quantidade de tinta necessária.

altura = float(input('Insira a altura: '))
# Solicita ao usuário que insira a altura da parede e converte a entrada para um número decimal (float), armazenando em `altura`.

largura = float(input('Insira a largura: '))
# Solicita ao usuário que insira a largura da parede e converte a entrada para um número decimal (float), armazenando em `largura`.

area = altura * largura
# Calcula a área da parede multiplicando a altura pela largura e armazena o resultado na variável `area`.

tinta = area / 2
# Calcula a quantidade de tinta necessária, considerando que 1 litro de tinta cobre 2 metros quadrados, e armazena o resultado na variável `tinta`.

print(f'Sua parede tem a dimensão {largura} x {altura} e sua área é de {area}m² ')
# Exibe as dimensões da parede e a área calculada ao usuário.

print(f'Seria necessário {tinta} litros de tinta para pintar sua parede.')
# Informa ao usuário a quantidade de tinta necessária para pintar a parede, baseada na área calculada.
