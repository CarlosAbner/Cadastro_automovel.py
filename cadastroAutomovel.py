print('=-'*15)
print('CADASTRO DE CARROS')
print('=-'*15)

# variavis para armazenar os valores de total de carros da toyota
#  ''       ''      ''      ''      '' carros or modelos do mesmo ano
#  ''       ''      ''      ''      '' carros or modelos abaixo do ano de 2000
totCarros = totAnos = abaixo2000 = 0

#loop definido para cadastro dos automoveis, MODELO, MARCA E ANO DE FABRICAÇÃO
while True:
    carro = str(input('Nome do automovel: ')).strip()
    marca = str(input('Marca do automovel : ')).strip()
    ano = int(input('Ano do automovel: '))
    if 'toyota' in marca:
        totCarros += 1
    if ano == 2022:
        totAnos += 1
    if carro or marca < 2000:
        abaixo2000 += 1 
#condição que permite ou não o cadastro de mais automoveis
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais automovel? ')).strip().upper()[0]
        print('=-'*15)
    if resp == 'N':
        break
#quando o programa terminado após a resp == N, imprime o resultado das varivais declaradas antes do while 
print(f'Temos {totCarros} da Toyota cadastrados')
print(f'Temos {totAnos} carros do ano de 2022')
print(f'Existe {abaixo2000} carros fabricados antes dos anos 2000')
