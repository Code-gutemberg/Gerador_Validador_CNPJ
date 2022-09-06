import re


def validador_cnpj(cnpj):
    if cnpj == '00.000.000/0000-00' or cnpj == '00000000000000':
        print('É uma sequencia Digite um CNPJ correto')
    else:
        cnpj = str(re.sub(r'[^0-9]', '', cnpj))
        cnpj_test01 = cnpj[0:4]
        cnpj_test02 = cnpj[4:12]
        cnpj_test03 = cnpj[0:5]
        cnpj_test04 = cnpj[5:13]
        range_01 = 6
        range_02 = 10
        range_03 = 7
        range_04 = 10
        sum_01 = 0
        sum_02 = 0
        sum_03 = 0
        sum_04 = 0
        sum_tot_01 = 0
        sum_tot_02 = 0

        for x in cnpj_test01:
            range_01 -= 1
            resultado_01 = int(x) * range_01
            sum_01 += resultado_01

        for y in cnpj_test02:
            range_02 -= 1
            resultado_02 = int(y) * range_02
            sum_02 += resultado_02

        sum_tot_01 = sum_01 + sum_02

        formula_01 = 11 - (sum_tot_01 % 11)

        if formula_01 <= 9:
            digito_1 = formula_01
        else:
            digito_1 = 0

        cnpj_test02_01 = cnpj[0:12] + str(digito_1)

        for h in cnpj_test03:
            range_03 -= 1
            resultado_03 = int(h) * range_03
            sum_03 += resultado_03

        for i in cnpj_test04:
            range_04 -= 1
            resultado_04 = int(i) * range_04
            sum_04 += resultado_04

        sum_tot_02 = sum_03 + sum_04

        formula_02 = 11 - (sum_tot_02 % 11)

        if formula_02 <= 9:
            digito_2 = formula_02
        else:
            digito_2 = 0

        cnpj_valido = cnpj_test02_01 + str(digito_2)
        if cnpj == cnpj_valido:
            print('O CNPJ foi VALIDADO COM SUCESSO!')
            print()
            print(f'{cnpj_valido[0:2]}.{cnpj_valido[2:5]}.'
                  f'{cnpj_valido[5:8]}/{cnpj_valido[8:12]}-'
                  f'{cnpj_valido[12:15]}')
            print('=' * 32)
            return True
        else:
            return False
