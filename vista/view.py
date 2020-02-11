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
    
    def mostrarTodo(self):
        
        self.app.layout = html.Div(children=[
        html.H1(children='Ventas por dia de la semana'),
    
        html.Div(children='''
            Dash: Amalio y Rafa
        '''),
        html.Div(
            [self.graphVentasDiasSemana("1")]
            , style={'width': '49%', 'float': 'right', 'display': 'inline-block'}
                 ),
        html.Div(
            [self.graphVentasDiasSemana("2","line")]
            , style={'width': '49%', 'float': 'right', 'display': 'inline-block'}
            )
    ])
        return 0;
        
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
    
    def definirLayout2(self):
        m = self.controler.cargarVentasDiasSemana()
        self.app.layout = html.Section(children=[
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

    def graphVentasDiasSemana(self,id,type='bar'):
        m = self.controler.cargarVentasDiasSemana()
        x=dcc.Graph(
            id='example-graph'+id,
            figure={
                'data': [
                    {'x': m[0], 'y': m[1], 'type': type, 'name': 'count'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
        return x
