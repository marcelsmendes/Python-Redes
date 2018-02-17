import random
import math
import colored

frase = '  curso em video python  '
color = bg('indian_red_1a') + fg('white')
reset = attr('reset')
print (color + 'Hello World !!!' + reset)
#print(frase[6::2])


#frase = frase.title().split()
#print(''.join(frase))

#frase[3] = frase[3].replace('Python','Android')
#print(''.join(frase))

n1 = float(input('Digite sua primeira nota'))
n2 = float(input('Digite sua segunda nota'))

m = (n1+n2)/2;
print('A sua média é {:.1f}'.format(m))

print('\033[0:35:44m Sua média foi boa')
    
