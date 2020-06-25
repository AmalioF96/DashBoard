'''
Created on 15 nov. 2019

@author: Amalio
'''
import pandas as pd
import numpy as np

original = pd.read_csv("C:/Users/Amalio/Desktop/tables/def/mArticulos.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode', encoding="latin_1");
nOriginal = np.array(original);
# obtenemos el total de facturas
indice = len(nOriginal);

i = 0;
j = 0;
destino = [];
while(i < indice):
    destino.append(nOriginal[i])
    if i % 5000 == 0 and i!=0:
        dt = pd.DataFrame(destino);
        cad="C:/Users/Amalio/Desktop/tables/def/artred/arts"+str(i)+".csv";
        print(cad)
        dt.to_csv(cad, index=False);
        print("Esto es i ", i);
        print("----------------");
        destino = [];
        j=0
    
    j = j + 1;
    i = i + 1;

print("Fin");
