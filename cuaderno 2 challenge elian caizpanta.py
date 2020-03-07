#!/usr/bin/env python
# coding: utf-8

# ![Título](Images/cisco.png)

# # Práctica de laboratorio: Delitos en San Francisco
# 
# ### Objetivos
# 
# Demuestre sus conocimientos acerca del ciclo activo del análisis de datos mediante un conjunto de datos determinado, herramientas, Python y la libreta de anotaciones de Jupyter.
# 
# #### Parte 1: Importar los paquetes de Python
# #### Parte 2: Cargar los datos
# #### Parte 3: Preparar los datos
# #### Parte 4: Analizar los datos
# #### Parte 5: Visualizar los datos
# 
# ### Segundo plano/situación
# 
# En esta práctica de laboratorio, importará algunos paquetes de Python que nos necesarios para analizar un conjunto de datos que contiene información sobre delitos en San Francisco. Luego utilizará Python y Jupyter Notebook para preparar estos datos para su análisis, analizarlos, graficarlos y comunicar sus conclusiones.
# 
# ### Recursos necesarios
# 
# * 1 computadora con acceso a Internet
# * Raspberry Pi versión 2 o superior
# * Bibliotecas de Python: pandas, numpy, matplotlib, folium, datetime y csv
# * Archivos de datos: Map-Crime_Incidents-Previous_Three_Months.csv

# ## Parte 1: Importar los paquetes de Python
# 
# En esta sección, importará los paquetes de Python que son necesarios para el resto de esta práctica de laboratorio.
# #### numpy 
# NumPy es el paquete fundamental para computación científica con Python. Contiene entre otras cosas: un potente objeto de matriz N dimensional y funciones sofisticadas (difusión).
# #### pandas 
# Pandas es un código abierto, una biblioteca con licencia BSD autorizada que proporciona un alto rendimiento, estructuras de datos fáciles de usar y herramientas de análisis de datos para el lenguaje de programación de Python.
# #### matplotlib
# Matplotlib es una biblioteca gráfica para el lenguaje de programación de Python y su extensión matemática numérica NumPy.
# #### folium 
# Folium es una biblioteca para crear mapas interactivos.

# In[50]:


pip install numpy


# In[51]:


pip install pandas


# In[52]:


pip install matplotlib


# In[53]:


pip install folium


# In[54]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium 


# ## Parte 2: Cargar los datos
# 
# En esta sección, cargará el conjunto de datos de delitos en San Francisco y los paquetes de Python necesarios para analizarlo y visualizarlo.

# #### Paso 1: Cargar los datos de delitos en San Francisco en un marco de datos.
# En este paso, se importarán los datos de delitos en San Francisco de un archivo de valores separado por comas (csv) en una trama de datos.

# In[55]:


# code cell 2
# This should be a local path
dataset_path = './Data/Map-Crime_Incidents-Previous_Three_Months.csv'

# read the original dataset (in comma separated values format) into a DataFrame
SF = pd.read_csv(dataset_path)


# Para ver las primeras cinco líneas del archivo csv, se utilizará el comando 'head' de Linux.

# In[56]:


# code cell 3
#!head -n 5 ./Data/Map-Crime_Incidents-Previous_Three_Months.csv
SF.head(5)


# #### Paso 2: Ver los datos importados.
# 
# A) Al ingresar el nombre del marco de datos en una celda, puede visualizar las filas superior e inferior de manera estructurada.

# In[57]:


# Code cell 4
pd.set_option('display.max_rows', 10) #Visualize 10 rows 
SF


# b) Utilice la función 'columns' para ver el nombre de las variables en el marco de datos.

# In[68]:


# Code cell 5
SF.columns


# ¿Cuántas variables se incluyen en el marco de datos de SF (ignore el índice)?

# 14

# c) Utilice la función 'len' para determinar la cantidad de filas en el conjunto de datos.

# In[60]:


# Code cell 6
len(SF)


# ## Parte 3: Preparar los datos
# 
# Ahora que cuenta con los datos cargados en el entorno de trabajo y determinó el análisis que desea realizar, es momento de preparar los datos para el análisis.
# 

# #### Paso 1: Extraer el mes y el día del campo de Date (Fecha).

# 'lambda' es una palabra clave de Python que define las reconocidas *funciones anónimas*. 'lambda' le permite especificar una función en una línea de código sin utilizar 'def' y sin definir un nombre específico para ella. La sintaxis para una expresión 'lambda' es:
# 
# 'lambda' *parámetros*: *expresión*.
# 
# En este caso, la función 'lambda' se utiliza para crear una función en línea que seleccione solo los dígitos del mes de la variable Date (Fecha) e 'int' para convertir una representación de secuencia en un valor entero. Luego, la función *pandas* 'apply' se utiliza para aplicar esta función a una columna entera (en la práctica, 'apply' define implícitamente un bucle 'for' y pasa una por una las filas a la función 'lambda').  El mismo procedimiento se puede hacer para el día. 

# In[61]:


# Code cell 7
SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))
print (SF)


# Para verificar que estas dos variables se agreguen al marco de datos de SF, use la función 'print' para imprimir algunos de los valores de estas columnas y 'type' para verificar que estas columnas nuevas contengan, de hecho, valores numéricos.

# In[62]:


# Code cell 8
print(SF['Month'][0:2])
print(SF['Day'][0:2])


# In[63]:


# Code cell 9
print(type(SF['Month'][0]))


# #### Paso 2: Eliminar las variables del marco de datos de SF.

# a) La columna 'IncidntNum' contiene varias celdas con NaN. En este caso, faltan los datos. Además, 'IncidntNum' no proporciona ningún valor al análisis. La columna se puede descartar del marco de datos. Una manera de eliminar variables que no desea en un marco de datos es mediante la función 'del'.

# In[64]:


# Code cell 10
del SF['IncidntNum']


# b) De manera similar, el atributo 'Location' no se incluirá en este análisis. Puede descartarse del marco de datos. 
# <p>O bien, puede usar la función 'drop' en el marco de datos y especificar que el *eje* es el 1 (0 para las filas) y que el comando no requiere una asignación a otro valor para almacenar el resultado (*inplace = True*).

# In[65]:


# Code cell 11
SF.drop('Location', axis=1, inplace=True )


# c) Verifique que se hayan eliminado las columnas.

# In[66]:


# Code cell 12
SF.columns


# ## Parte 4: Analizar los datos
# 
# Ahora que el marco de datos se ha elaborado con datos, es momento de analizar los datos. 

# #### Paso 1: Resumir las variables para obtener información estadística.
# 
# a) Utilice la función 'value_counts' para resumir la cantidad de delitos cometidos por tipo; luego seleccione 'print' para visualizar los contenidos de la variable *CountCategory*.

# In[69]:


# Code cell 13
CountCategory = SF['Category'].value_counts()
print(CountCategory)


# b) De manera predeterminada, los conteos se ordenan de forma descendente. El valor del parámetro opcional *ascendente* se puede configurar en *True* para invertir este comportamiento.

# In[70]:


# Code cell 14
SF['Category'].value_counts(ascending=True)


# ¿Qué tipo de delitos se cometió más?

# LARCENY/THEFT

# c) Al jerarquizar las dos funciones en un comando, puede lograr el mismo resultado con una línea de
# código.

# In[71]:


# Code cell 15
print(SF['Category'].value_counts(ascending=True))


# **Pregunta de desafío**: ¿Qué PdDistrict presentaba la mayoría de los incidentes de delitos informados? Proporcione los comandos de Python
# utilizados para apoyar su respuesta.

# In[72]:


print(SF['PdDistrict'].value_counts(ascending=True))


# SOUTHERN

# #### Paso 2: Crear subconjuntos de datos y organizarlos en marcos de datos más pequeños.

# a) La indexación lógica se puede utilizar para seleccionar únicamente las filas en las cuales se cumple una condición específica. Por ejemplo, el código siguiente recupera sólo los delitos cometidos en agosto y guarda el resultado en un nuevo marco de datos.

# In[79]:


# Code cell 16
AugustCrimes = SF[SF['Month'] ==8]
print(AugustCrimes)


# ¿Cuántos incidentes de delitos hubo en agosto? 

# 9720

# ¿Cuántos robos se informaron en agosto?

# 1257

# In[80]:


# code cell 17
# Possible code for the question: How many burglaries were reported in the month of August?
AugustCrimes = SF[SF['Month'] == 8]
AugustCrimesB = SF[SF['Category'] == 'BURGLARY']
len(AugustCrimesB)


# b) Para crear un subconjunto del marco de datos de SF para un día específico, use la función 'query' para comparar el mes y el día al mismo tiempo.

# In[81]:


# Code cell 18
Crime0704 = SF.query('Month == 7 and Day == 4')
Crime0704


# In[82]:


# Code cell 19
SF.columns


# ## Parte 5: Presentar los datos
# 
# La visualización y presentación de datos proporciona una descripción general inmediata que puede no ser evidente simplemente
# observando los datos sin procesar. El marco de datos de SF contiene las coordenadas de longitud y latitud que se pueden utilizar para
# graficar los datos.

# #### Paso 1: Graficar el marco de datos de SF con las variables X e Y.

# a) Utilice la función 'plot()' para graficar el marco de datos de SF. Utilice el parámetro opcional para crear el gráfico en rojo y configurar la forma del marcador en un círculo utilizando *ro*.

# In[103]:


# Code cell 20
plt.plot(SF['X'],SF['Y'], 'b')
plt.show()


# b) Identifique la cantidad de distritos de departamentos policiales y luego cree el diccionario *pd_districts* para asociar la secuencia a un valor entero.

# In[84]:


# Code cell 21
pd_districts = np.unique(SF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))
pd_districts_levels


# c) Utilice 'apply' y 'lambda' para agregar la ID del valor entero del departamento policial a una nueva columna para el marco de datos. 

# In[86]:


# Code cell 22
SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts_levels[row])


# d) Utilice el *PdDistrictCode* creado recientemente para cambiar automáticamente el color.

# In[87]:


# Code cell 23
plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
plt.show()


# #### Paso 2: Agregar los paquetes de mapas para mejorar el gráfico.

# En el paso 1, creó un gráfico simple que muestra dónde ocurrieron los incidentes de delitos en el condado de SF. Este gráfico
# es útil, pero 'folium' ofrece funciones adicionales que permiten superponer este gráfico en un mapa de OpenStreet. 

# a) 'Folium' requiere que se especifique el color del marcador mediante un valor hexadecimal. Por este motivo, utilizamos el paquete *colores* y seleccionamos los colores necesarios.

# In[88]:


# Code cell 24
from matplotlib import colors
districts = np.unique(SF['PdDistrict'])
print(list(colors.cnames.values())[0:len(districts)]) 


# b) Cree un diccionario de colores para cada distrito del departamento policial.

# In[89]:


# Code cell 25
color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)])) 
color_dict


# c) Cree el mapa con las coordenadas centrales de los datos de SF para centrar el mapa (utilice 'mean'). Para reducir el tiempo de cómputo, se utiliza *plotEvery* para limitar la cantidad de datos graficados. Establezca este valor a 1 para graficar todas las filas (puede llevar mucho tiempo visualizar el mapa).

# In[99]:


# Code cell 26
#Create map
map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoomstart = 12)
plotEvery = 50
obs = list(zip( SF['Y'], SF['X'], SF['PdDistrict'])) 

for el in obs[0:-1:plotEvery]: 
    
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fillcolor=el[2],radius=10).add_to(map_osm)
    


# In[100]:


# Code cell 27
map_osm


# <font size='0.5'>&copy; 2017 Cisco y/o sus filiales. Todos los derechos reservados. Este documento es información pública de Cisco.<font>
