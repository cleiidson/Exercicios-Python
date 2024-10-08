#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = float(input('Me informe um valor em metros: '))
# Solicita ao usuário que insira um valor em metros e converte a entrada para um número decimal (float), armazenando na variável `m`.

c = m * 100
# Calcula o equivalente em centímetros (1 metro = 100 centímetros) e armazena o resultado na variável `c`.

mm = m * 1000
# Calcula o equivalente em milímetros (1 metro = 1000 milímetros) e armazena o resultado na variável `mm`.

print('Agora irei converter ele em centímetros\n'
      f'{c} cm e em milímetros se torna {mm} mm')
# Exibe os resultados da conversão de metros para centímetros e milímetros, formatando a saída de forma clara.
