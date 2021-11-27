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
data['Nombre municipio'].unique().shape[0]

#3. Liste los municipios afectados (sin repetirlos)
data['Nombre municipio'].unique().shape[0]


# 4. Número de personas que se encuentran en atención en casa
data.groupby('Ubicación del caso').size()
data['Ubicación del caso'].replace('CASA','Casa',inplace=True)
data['Ubicación del caso'].replace('casa','Casa',inplace=True)
data[(data['Ubicación del caso'] == 'Casa')].groupby('Ubicación del caso').size()

#5. Número de personas que se encuentran recuperados
data.columns
data.groupby('Recuperado').size()
data['Recuperado'].replace('fallecido','Fallecido',inplace=True)

data[(data['Recuperado'] == 'Recuperado')].groupby('Recuperado').size()


# 6. Número de personas que ha fallecido
data.groupby('Estado').size()

data[data['Estado'] == 'Fallecido'].groupby('Estado').size()


# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,Relacionado)
data[(data['Tipo de contagio'] == 'Importado') | 
     (data['Tipo de contagio'] == 'En estudio') | 
     (data['Tipo de contagio'] == 'Relacionado')].groupby('Tipo de contagio').size().sort_values(ascending=True)


# 8. Número de departamentos afectados
data.columns
data['Nombre departamento'].replace('Tolima','TOLIMA',inplace=True)
data['Nombre departamento'].replace('BARRANQUILLA','ATLANTICO',inplace=True)
data['Nombre departamento'].replace('Caldas','CALDAS',inplace=True)
data['Nombre departamento'].replace('STA MARTA D.E.','MAGDALENA',inplace=True)
data['Nombre departamento'].replace('CARTAGENA','BOLIVAR',inplace=True)
data['Nombre departamento'].replace('BOGOTA','CUNDINAMARCA',inplace=True)
data.groupby('Nombre departamento').size()

data.groupby('Nombre departamento').size().count()


# 9. Liste los departamentos afectados(sin repetirlos)
data['Nombre departamento'].unique().shape[0]


# 10. Ordene de mayor a menor por tipo de atención
data.columns
data.groupby('Tipo de contagio').size().sort_values(ascending=True)


# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados
data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10)



# 12 Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)








