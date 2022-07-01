from os import listdir
import os

Ruta = 'C:/Users/ZTE/Desktop/TALLER 3'

contenido = os.listdir(Ruta)
archivos = []
for archivo in contenido:
     if archivo.startswith('P'):
      print("El nombre del archivo es:",archivo, "la extencion es:", archivo[12:16], "y la ruta es:", Ruta)
      
     if archivo.startswith('S'):
      print("El nombre del archivo es:",archivo, "la extencion es:", archivo[9:14], "y la ruta es:", Ruta)

     if archivo.startswith('u'):
      print("El nombre del archivo es:",archivo, "la extencion es:", archivo[8:12], "y la ruta es:", Ruta)
else:
      print("no existen mas archivos")

with open("C:/Users/ZTE/Desktop/TALLER 3/usuarios.csv","r") as archivo:

     print("\nEl contenido del archivo usuarios.csv es:")
     for linea in archivo:
        print("\n",linea)

import csv
with open("C:/Users/ZTE/Desktop/TALLER 3/usuarios.csv") as file:
    reader = list(file)
    for row in reader:
        print (row)
        
import pandas as pd 

fields = ['Nombre', 'Apellidos', 'Dependencia', 'Estado']
df = pd.read_csv ('C:/Users/ZTE/Desktop/TALLER 3/usuarios.csv', usecols=fields, sep=';')
print (df)


df = pd.read_csv (r"C:/Users/ZTE/Desktop/TALLER 3/usuarios.csv")

total_cols = len (df.axes[0])
print ("Número total de columnas: " +str(total_cols))

