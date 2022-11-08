from random import randint
from time import sleep
jogo = {'primeira jogada': randint(1, 11),
        'segunda jogada': randint(1, 11)}
print('a jogada foi')
for k, v in jogo.items():
        print(f'{k}primeira jogada foi {v}')
        sleep(7)
