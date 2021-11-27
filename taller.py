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

data.groupby('Estado').size()
data.Sexo.replace('f','F',inplace=True)
data.Sexo.replace('m','M',inplace=True)

data.groupby('Sexo').size()
data.Estado.replace('leve','Leve',inplace=True)
data.Estado.replace('LEVE','Leve',inplace=True)


# Realice las líneas de código en Python que den respuesta a las siguientes preguntas:
# 1. Número de casos de Contagiados en el País.
data.shape[0]

# 2. Número de Municipios Afectados
data.groupby('Nombre departamento').unique().shape()









