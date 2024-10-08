#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('Digite um número para que eu possa mostrar o seu dobro, triplo e raíz quadrada.')
# Exibe uma mensagem informativa ao usuário sobre o que o programa fará.

n1 = int(input('Digite um número: '))
# Solicita ao usuário que insira um número e armazena o valor na variável `n1`, convertendo a entrada para um inteiro.

dobro = n1 * 2
# Calcula o dobro do número `n1` e armazena o resultado na variável `dobro`.

triplo = n1 * 3
# Calcula o triplo do número `n1` e armazena o resultado na variável `triplo`.

raizQ = n1 ** (1/2)
# Calcula a raiz quadrada de `n1` utilizando a exponenciação e armazena o resultado na variável `raizQ`.

print(f'O dobro de {n1} é {dobro},\n'
      f'o triplo é {triplo},\n'
      f'a raíz quadrada é {raizQ:.2f}')
# Exibe os resultados das operações de forma formatada, mostrando 2 casas decimais para a raiz quadrada.
