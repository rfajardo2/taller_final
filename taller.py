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
data['Nombre municipio'].replace('puerto COLOMBIA','PUERTO COLOMBIA',inplace=True)
data['Nombre municipio'].replace('puerto colombia','PUERTO COLOMBIA',inplace=True)
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
data.groupby('Ubicación del caso').size().sort_values(ascending=False)


# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados
data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10)



# 12 Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)


# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados

data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)



# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados

data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10)


# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos

data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)


# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados

data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)


# 17. Liste agrupado por departamento y en orden de Mayor a menor las 
# ciudades con mas casos de contagiados

# data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values(ascending=False)..head(10)
# prueba_D_N = data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values()
# prueba_D_N = data.groupby(['Nombre municipio']).size().sort_values(ascending=False)

# data.groupby(['Nombre departamento','Nombre municipio']).size().apply(lambda x: x.sort_values(["0"], ascending = False))
# data(['Nombre departamento','Nombre municipio'])


# ppp=data.groupby(['Nombre departamento','Nombre municipio']).agg({'Sexo':sum})

# prueba_D_N.columns
# prueba_D_N['0']

# prueba_D_N.groupby(['Nombre municipio']).size()
# data.value_counts().sort_values(ascending=False)

# prueba_D_N =.sort_values(ascending=False)
# prueba_D_N2 =prueba_D_N.groupby(['Nombre departamento','Nombre municipio']).size()
# prueba_D_N =data.groupby(['Nombre departamento'])
# prueba_D_N.columns()


data.groupby(['Nombre departamento','Nombre municipio']).size()



# 18. Número de Mujeres y hombres contagiados por ciudad por departamento

data.groupby(['Nombre departamento','Nombre municipio','Sexo']).size()

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
data.columns




# 20. Liste de mayor a menor el número de contagiados por país de procedencia
data.groupby('Nombre del país').size().sort_values(ascending=False)


# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios

data.groupby('Fecha de diagnóstico').size().sort_values(ascending=False)



# 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombmia



data.Estado.value_counts().plot


data.Estado.value_counts().plot

data.groupby('Ubicación del caso').size().plot.bar()
data.groupby('Tipo de contagio').size().sort_values


# 25
data.groupby(['Nombre municipio','Ubicación del caso']).size()



# 27 
data.Recuperado.value_counts().plot()


# 29. Grafique las curvas de contagio, muerte y recuperación de las 10 ciudades con mas casos de contagiados acumulados


data.Recuperado.value_counts()
data.groupby(['Nombre municipio','Recuperado']).size().head(10).plot()
data.groupby(['Nombre municipio','Recuperado']).size().sort_values(ascending=False).head(10).plot()
data.Recuperado.value_counts().plot.bar()


# 30. Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia.

data[(data['Estado'] == 'Fallecido')].groupby('Edad').size().sort_values(ascending=False)


# 32. Haga un gráfico de barras por atención de toda Colombi
data['Ubicación del caso'].value_counts().plot.bar()

# 33. Haga un gráfico de barras por Sexo de toda Colombia
data.Sexo.value_counts().plot.bar()

# 34. Haga un gráfico de barras por tipo de toda Colombia

data['Tipo de contagio'].value_counts().plot.bar()


# 35. Haga un gráfico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia

data.Recuperado.value_counts().plot.bar()











