'''CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO
UMA MENSAGEM NO FINAL, DE ACORDO COM A MEDIA ATINGIDA:
-MEDIA ABAIXO DE 5.0: REPROVADO
-MEDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
-MEDIA 7.0 OU SUPERIOR: APROVADO'''

# Leitura das notas
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, a média do aluno é {media}')

if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')