'''FAÇA UMA TABUADA, MOSTRANDO O NÚMERO QUE O USUARIO ESCOLHER, UTILIZANDO FOR'''
# Solicita um número para gerar a tabuada
tabuada = int(input('Digite um número para ver a tabuada: '))

# Mostra o cabeçalho da tabuada
print(f'Tabuada do {tabuada}')

# Laço para calcular e mostrar a tabuada de 1 a 10
for c in range(1, 11):
    print(f'{tabuada} x {c:2} = {c * tabuada}')  # Exibe a linha da tabuada
