#Desafio 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, moestre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

anoatual = datetime.date.today().year
novo = 0
velho = 0
for c in range(1,8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if (anoatual - 18)<=ano<=anoatual:
        novo = novo + 1
    else:
        velho = velho + 1
print(f'Há {novo} pessoas menores de idade. ')
print(f'Há {velho} pessoas maiores de idade. ')

