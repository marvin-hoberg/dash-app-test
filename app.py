from dash import Dash, html, dcc
import plotly.express as px
import os 


app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello Dash - testing")
])


if __name__ == "__main__":

    app.run_server(
        debug=True, 
        host="localhost", 
        port=8081)