'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7.00 por cada km acima do limite.'''

# Solicita ao usuário a velocidade do carro
velo = int(input('A velocidade da via é 80Km/h, qual a velocidade que você estava? '))

# Verifica se a velocidade está dentro do limite de 80 km/h
if velo <= 80:
    # Se a velocidade estiver dentro do limite, informa que está tudo certo
    print('Você estava no limite permitido. Pode seguir viagem!')
else:
    # Se a velocidade estiver acima do limite, calcula a multa
    multa = (velo - 80) * 7
    # Mostra o valor da multa
    print(f'Você estava acima do permitido. Será multado no valor de R${multa},00 ')
