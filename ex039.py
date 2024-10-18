'''Mundo Python 2 - Condições Aninhadas'''
nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Cleidson':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Francisco' or nome == 'Antonio':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Joana Lara Marcia Julia': #Trocando o or por in
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}.')