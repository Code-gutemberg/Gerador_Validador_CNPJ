from random import randint
from gerador import gerador_cnpj
from validador import validador_cnpj


print('======== GERADOR DE CPF ========')
# Gerador de Números aleatórios
numero = str(randint(10000000000000, 99999999999999))
while validador_cnpj(gerador_cnpj(numero)) is False:
    numero = str(randint(10000000000000, 99999999999999))
