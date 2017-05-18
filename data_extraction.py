# coding=utf8

import requests

import numpy as np
import statsmodels.api as sm

from config import modelo


ACCIONES = ['EXITO', 'ECOPETROL', 'BCOLOMBIA', 'CORFICOLCF', 'PFBCOLOM','GRUPOSURA', 'PFAVAL', 'NUTRESA', 'PFGRUPSURA'
            'ISA', 'CEMARGOS', 'GRUPOARGOS', 'PFGRUPOARG', 'PFDAVVNDA', 'ICOLCAP', 'EEB', 'CLH', 'CELSIA','PFCEMARGOS',
            'PFAVH', 'GRUPOAVAL', 'CNEC', 'HCOLSEL', 'BOGOTA', 'ICOLRISK', 'ETB', 'MINEROS', 'BBVACOL', 'CONCONCRET',
            'PFCARPAK', 'BVC', 'ENKA', 'ELCONDOR', 'PFCORFICOL', 'CARTON', 'FABRICATO', 'COLTEJER'
]


def organizar_matriz(prices, modelo):
    matriz = np.empty([365*2, len(modelo)+1])
    for row in len(matriz)[0]:
        matriz[row, 0] = prices[row]
        matriz[row, 1] = prices[row + 1]
        matriz[row, 2] = prices[row + 2]
        matriz[row, 3] = prices[row + 3]

    return matriz


for ACCION in ACCIONES:
    r = requests.get(('https://www.bvc.com.co/mercados/GraficosServlet?home=no&tipo=ACCION&mercInd=RV&nemo={0}&tiempo=ayer').format(ACCION))
    datos = r.content
    matriz = np.empty([len(datos), 1])
    i = 0

    for line in datos.split(b'\n'):
        movimiento_diario = line.split(b',')
        try:
            matriz[i, 0] = movimiento_diario[1]
            i = i + 1
        except:
            pass

    nueva_matriz = organizar_matriz(prices=matriz, modelo=modelo)
    print(nueva_matriz)
#results = sm.OLS(y, X).fit()

