'''
Created on 29 dic. 2019

@author: Amalio
'''
import dash
from vista.view import view


if __name__ == '__main__':
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    miVista=view(app)
    miVista.mostrarTodo()
    app.run_server(debug=True)
