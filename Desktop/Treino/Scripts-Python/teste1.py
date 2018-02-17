dia  = int(input('Qual é o dia do seu nascimento?'))
mes = int(input('Qual é o mes do seu nascimento?'))
ano = int(input('Qual é o ano do seu nascimeto?'))

if dia < 10:
    d = '0' + str(dia)
if mes < 10:
    m = '0' + str(mes)

print(d,'/',m,'/',ano)
