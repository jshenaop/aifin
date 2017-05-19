##
i = 0
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fechas = ['2017-05-17 17:59', '2017-05-18 18:59', '2017-05-19 19:59', '2017-05-20 20:59']

# formato de fecha (2017-05-17 14:59)

import numpy as np

matrix_fechas = np.zeros((2, 3))
matrix_valores = np.zeros((9, 1))
# second_col = matrix[:,1,:]
# print(matrix_fechas)
# print(matrix_valores)

for valor in valores:
    matrix_valores[i, 0] = valor
    i = i + 1
print(matrix_valores)
