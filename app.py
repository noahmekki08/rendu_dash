import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialisation de l'application
app = dash.Dash(__name__)

# Mise en page
app.layout = html.Div([
    html.H1("Mon application Dash"),
    dcc.Input(id="input", type="text", placeholder="Entrez quelque chose..."),
    html.Div(id="output")
])

# Callback pour mettre à jour la sortie
@app.callback(
    Output("output", "children"),
    [Input("input", "value")]
)
def update_output(value):
    if value:
        return f"Vous avez saisi : {value}"
    return "Entrez un texte pour voir un résultat."

# Lancement de l'application
if __name__ == "__main__":
    app.run_server(debug=True)
