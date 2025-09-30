from dash import Dash, dcc, html, Input, Output 
import plotly.express as px 
import plotly.data as pldata 

df = px.data.gapminder()

# Initialize Dash app
app = Dash(__name__) 


app.layout = html.Div([ 
    dcc.Dropdown( 
        id="country-dropdown", 
        options=[{"label": c, "value": c} for c in sorted(df["country"].unique())], 
        value="Canada", 
    ),
    dcc.Graph(id="gdp-growth") 
])

# Callback for dynamic updates
@app.callback( 
    Output("gdp-growth", "figure"),  
    [Input("country-dropdown", "value")] 
)
def update_graph(country): 
    dff = df[df["country"] == country]
    fig = px.line(dff, x="year", y="gdpPercap", title=f"{country} gdp")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 