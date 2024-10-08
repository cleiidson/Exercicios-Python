#faça um programa que leia uma frase pelo tecldo e mostre:
'''quantas vezes aparece a letra 'A'.
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a ultima vez'''

# Solicita que o usuário escreva uma frase, remove espaços extras e converte para minúsculas
frase = input('Escreva uma frase: ').strip().lower()

# Conta quantas vezes a letra 'a' aparece na frase (agora sempre em minúsculas)
print(f'A letra (A) aparece {frase.count("a")}x')

# Encontra a primeira ocorrência da letra 'a' na frase (em minúsculas) e soma 1 para ser intuitivo ao usuário
print(f'A letra (A) aparece primeiro na posição {frase.find("a") + 1}')  # Acrescentando +1 para ser desconsiderada a posição 0

# Mostra a posição da última ocorrência da letra 'a' e soma 1 para seguir a lógica de contagem a partir de 1
print(f'A letra (A) aparece por último na posição {frase.rfind("a") + 1}')  # Acrescentando +1 para ser desconsiderada a posição 0

