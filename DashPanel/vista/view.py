'''
Created on 29 dic. 2019

@author: Amalio
'''
import dash
import dash_core_components as dcc
import dash_html_components as html

from controlador.controlador import ControladorApp
from prueba import definirLayout


class view():

    def __init__(self,app):
        self.controler = ControladorApp()
        self.app=app
        definirLayout()
        
    def definirLayout(self):
        m = self.controler.cargarVentasDiasSemana()
        self.app.layout = html.Div(children=[
        html.H1(children='Ventas por dia de la semana'),
    
        html.Div(children='''
            Dash: Amalio y Rafa
        '''),
        
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': m[0], 'y': m[1], 'type': 'bar', 'name': 'count'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ])
        return 0

