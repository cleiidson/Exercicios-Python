'''CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM POLINDROMO,
DESCONSIDERANDO OS ESPAÇOS.
EX APOS A SOPA
# Removendo todos os espaços e exibindo o número de caracteres restantes
semEspaço = nome.replace(" ", "")
'''
# Solicita ao usuário que escreva uma frase e remove espaços em branco no início e no fim
frase = str(input('Escreva uma frase para saber se ela é um políndromo: ')).strip().lower()

# Remove todos os espaços da frase
semEspaço = frase.replace(" ", "")

# Inverte a string sem espaços
invertido = semEspaço[::-1]

# Compara a string original (sem espaços) com a string invertida
if semEspaço == invertido:
    # Se forem iguais, é um palíndromo
    print(f'A frase "{frase}" é um políndromo')
else:
    # Se não forem iguais, não é um palíndromo
    print(f'A frase "{frase}" não é um políndromo.')
