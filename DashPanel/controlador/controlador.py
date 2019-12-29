'''
Created on 29 dic. 2019

@author: Amalio
'''

_URL = 'bolt://localhost:11005'
_USER = 'neo4j'
_PASSWORD = '123'

from modelo.Connection import Connection

class ControladorApp(object):
    
    def __init__(self):
        self.crearConexion()
        
        
    def crearConexion(self):
            Connection.__init__(self , _URL , _USER , _PASSWORD)
            
    def cargarVentasDiasSemana(self):
        result=list(Connection.ventasPorDiaSemana(self))
        
        i=0;
        matriz=[["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo",],[0,0,0,0,0,0,0]];
        
        for record in result:
            matriz[1][i]=record["CO"]
            i+=1

        return matriz

if __name__ == '__main__':
    c=ControladorApp()
    