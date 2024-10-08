#Testando cores no terminal

a = 3
b = 5
print(f'Os valores são \33[32m{a}\33[m e \33[31m{b}\33[m!!!')

nome = 'CLEIDSON'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoBranco':'\033[7:30m'}
print(f'Olá! Muito prazer em te conhecer. {cores["pretoBranco"]}{nome}{cores["limpa"]}')



'''
    Estrutura dos Códigos ANSI:

O padrão básico é: \033[estilo;textcor;backgroundm

\033 é o código de escape.

estilo é o estilo de formatação (normal, negrito, sublinhado, etc.).

textcor é a cor do texto.

background é a cor de fundo.

    Códigos de Estilos:
0 = Reset/Normal (sem formatação)
1 = Negrito
4 = Sublinhado
7 = Invertido (cor do texto e do fundo trocadas)

    Códigos de Cores do Texto:
30 = Preto
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul
35 = Magenta
36 = Ciano
37 = Branco

    Códigos de Cores de Fundo:
40 = Fundo Preto
41 = Fundo Vermelho
42 = Fundo Verde
43 = Fundo Amarelo
44 = Fundo Azul
45 = Fundo Magenta
46 = Fundo Ciano
47 = Fundo Branco

    Exemplos de Códigos ANSI:
Texto Verde (normal):
\033[32m

Texto Vermelho Negrito:
\033[1;31m

Texto Azul Sublinhado:
\033[4;34m

Texto Branco com Fundo Azul:
\033[37;44m

Texto Amarelo com Fundo Preto e Negrito:
\033[1;33;40m

Texto Invertido (Preto no Branco):
\033[7m

Resetar formatação (voltar ao normal):
\033[m ou \033[0m
'''