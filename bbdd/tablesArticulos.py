'''
Created on 15 nov. 2019

@author: Amalio
'''
import pymysql
import pandas as pd
import numpy as np
# from macpath import split

original = pd.read_csv("C:/Users/Amalio/Desktop/tables/def/mArticulos.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode', encoding="latin_1");
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
print("ARTICULOS")
while(i < indice):
    cad1 = str(nOriginal[i])
    cad1 = cad1.replace("[", "");
    cad1 = cad1.replace("]", "");
    cad1 = cad1.replace("nan", "'null'");
    cad1 = cad1.replace("\n", "' '");
    cad1 = cad1.replace("' ' '", "' '");
    cad1 = cad1.replace("''", "'");
    cad1 = cad1.replace(",", ".");
    cad1 = cad1.replace("' '", "','");
    x = 0
    prueba1 = "id,descripcion,marca_id,precio_con_iva,compra_caja,dias_vencimiento,mayorista_con_iva,mayorista_sin_iva,id_tipo_compra,id_concepto_art,fecha_modificacion_precio,exclusivo,sugerido,id_motivo_inactivacion,fecha_modificacion_costo,precio_con_iva2,familia_id,unidad,procesado,id_interno,impuesto_id,costo_sin_iva,costo_con_iva,id_procedencia,id_tp_envasado,contenido_caja,id_tp_articulo,recargo,proveedor_id,activo,fecha_act,precio_sugerido,activo_venta,etiqueta,imprimir_fecha_vencimiento,venta_restaurant,venta_regimen_turismo,fecha_act_precio".split(",")
    prueba2 = cad1.split(",")
    # print(len(prueba1), "---", len(prueba2))
    # for ind in range(0, len(prueba2)):
    #    if ind < len(prueba1):
    #        print("index: ", ind, "\t", prueba1[ind], "\t\t", prueba2[ind], "\n");
    #    else:
    #        print("index: ", ind, "\t", "None Bro\t", prueba2[ind], "\n");
    # End for
    cad = "INSERT INTO articulos(id,descripcion,marca_id,precio_con_iva,compra_caja,dias_vencimiento,mayorista_con_iva,mayorista_sin_iva,id_tipo_compra,id_concepto_art,fecha_modificacion_precio,exclusivo,sugerido,id_motivo_inactivacion,fecha_modificacion_costo,precio_con_iva2,familia_id,unidad,procesado,id_interno,impuesto_id,costo_sin_iva,costo_con_iva,id_procedencia,id_tp_envasado,contenido_caja,id_tp_articulo,recargo,proveedor_id,activo,fecha_act,precio_sugerido,activo_venta,etiqueta,imprimir_fecha_vencimiento,venta_restaurant,venta_regimen_turismo,fecha_act_precio) VALUES(" + cad1 + ")";
    try:
        if(len(prueba1) == len(prueba2)):
            exe = cursor.execute(cad);
    except Exception as err:
            contErrores += 1
        
    if i % 5000 == 0 and i != 0:
        print("Esto es i:", i, "Errores:", contErrores);
        print("----------------");
    i = i + 1;

print("Fin");

# some other statements  with the help of cursor
connection.commit();
connection.close()

if __name__ == '__main__':
    print("Hola")
