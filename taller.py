# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:53:48 2021

@author: Desarrollo         
"""


import pandas as pd

url = 'covid_22_noviembre.csv'

data = pd.read_csv(url)

# tamaño del data set
data.shape
# columnas del data set
data.columns

# Realice las líneas de código en Python que den respuesta a las siguientes preguntas:
# 1. Número de casos de Contagiados en el País.
data.shape[0]


