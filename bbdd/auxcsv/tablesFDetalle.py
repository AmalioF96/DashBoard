'''
Created on 15 nov. 2019

@author: Amalio
'''
import pymysql
import pandas as pd
import numpy as np
# from macpath import split

original = pd.read_csv("C:/Users/Amalio/Desktop/tables/def/mFacturaDetalle.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode', encoding="latin_1");
nOriginal = np.array(original);
# obtenemos el total de facturas
indice = len(nOriginal);

i = 0;
j = 0;
contErrores = 0;

destino = [];
# database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="sistemarecomendador")
cursor = connection.cursor()
print("FACTURA DETALLE")
while(i < indice):
    cad1 = str(nOriginal[i])
    cad1 = cad1.replace("[", "");
    cad1 = cad1.replace("]", "");
    cad1 = cad1.replace("nan", "'nan'");
    cad1 = cad1.replace("\n", "' '");
    cad1 = cad1.replace("' ' '", "' '");
    cad1 = cad1.replace("''", "'");
    cad1 = cad1.replace(",", ".");
    cad1 = cad1.replace("' '", "','");
    x = 0
    prueba1 = "factura_id,codigo,precio,cantidad".split(",")
    prueba2 = cad1.split(",")

    cad = "INSERT INTO `facturadetalle`(`factura_id`, `codigo`, `precio`, `cantidad`) \
     VALUES(" + cad1 + ")";
   
    try:
            exe = cursor.execute(cad);
    except Exception as err:
            contErrores += 1
            print(err)
        
    if i % 5000 == 0 and i != 0:
        print("Esto es i:", i, "Errores:", contErrores);
        print("----------------");
    i = i + 1;
connection.commit();
print("Fin");

# some other statements  with the help of cursor
connection.close()

if __name__ == '__main__':
    print("Hola")
