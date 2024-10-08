frase = 'Curso em Video Python'

# Fatiando a frase do índice 1 até o 14 (lembrando que o final é exclusivo) de 3 em 3
print(frase[1:15:3])

# Contando quantos 'O' maiúsculos tem na frase
print(frase.count('O'))

# Convertendo a frase para maiúscula e contando quantas letras 'O' existem
print(frase.upper().count('O'))

# Verificando o tamanho da frase (quantidade de caracteres)
print(len(frase))

# Removendo espaços no início e no final da frase e verificando o novo tamanho
print(len(frase.strip()))

# Substituindo 'Python' por 'Android' na frase, mas sem alterar a original
print(frase.replace('Python', 'Android'))

# A frase original continua inalterada, pois não foi salvo o resultado da substituição
print(frase)

# Agora sim, salvando a substituição para que a alteração seja permanente
frase = frase.replace('Python', 'Android')
print(frase)

# Verificando se a palavra 'Curso' está na frase (retorna True ou False)
print('Curso' in frase)

# Encontrando a posição onde a palavra 'Curso' começa na frase
print(frase.find('Curso'))

# Encontrando a posição onde a palavra 'Video' começa na frase
print(frase.find('Video'))

# Tentando encontrar a palavra 'curso' (com letra minúscula), o que não existe, então retorna -1
print(frase.find('curso'))

# Convertendo a frase para minúscula e encontrando a palavra 'video'
print(frase.lower().find('video'))

# Dividindo a frase em uma lista de palavras
dividido = frase.split()

# Mostrando a primeira palavra da lista
print(dividido[0])

# Mostrando a quarta letra da terceira palavra da lista
print(dividido[2][3])

frase = 'Curso em Video Python'

# Exemplo 1: Acessando a quarta letra da segunda palavra
dividido = frase.split()
print(dividido[1][3])  # 's' de 'em'

# Exemplo 2: Acessando a primeira letra da primeira palavra
print(dividido[0][0])  # 'C' de 'Curso'

# Exemplo 3: Acessando a última letra da última palavra
print(dividido[-1][-1])  # 'n' de 'Python'

# Exemplo 4: Acessando a terceira letra do segundo elemento da lista de palavras
print(dividido[2][2])  # 'd' de 'Video'

# Exemplo 5: Acessando caracteres da string em um slice
print(frase[6:10])  # 'em V'

# Exemplo 6: Acessando todas as letras de uma palavra, exceto a primeira
print(dividido[3][1:])  # 'ython', que é 'Python' sem a primeira letra

# Exemplo 7: Acessando todas as palavras a partir da terceira
print(dividido[2:])  # ['Video', 'Python']

# Exemplo 8: Invertendo a string
print(frase[::-1])  # 'nohtyP oediV me osruC'
