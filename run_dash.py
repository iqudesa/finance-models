import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html
from pathlib import Path

DATA_DIR = Path(__file__).parent

app = Dash(__name__)

def load_excel(name):
    return pd.read_excel(DATA_DIR / f"{name}.xlsx")

dcf = load_excel("dcf")
lbo = load_excel("lbo")
budget = load_excel("budget")

app.layout = html.Div([
    html.H1("Finance PRO Dashboard", style={"textAlign": "center", "background": "linear-gradient(90deg,#1e3a8a,#3b82f6)", "padding": "1rem", "color": "white"}),
    dcc.Tabs([
        dcc.Tab(label="DCF", children=[
            html.H3("Discounted Cash Flow"),
            dcc.Graph(figure=go.Figure()
                .add_trace(go.Bar(x=dcf["Year"], y=dcf["FCF"], name="FCF"))
                .add_trace(go.Scatter(x=dcf["Year"], y=dcf["PV"], name="PV", line=dict(color="orange")))
                .update_layout(title="DCF: FCF vs PV", xaxis_title="Year", yaxis_title="$M"))
        ]),
        dcc.Tab(label="LBO", children=[
            html.H3("Leveraged Buyout"),
            dcc.Graph(figure=go.Figure()
                .add_trace(go.Bar(x=lbo["Year"], y=lbo["EBITDA"], name="EBITDA"))
                .add_trace(go.Scatter(x=lbo["Year"], y=lbo["Net Debt"], name="Net Debt", line=dict(color="red")))
                .update_layout(title="LBO: EBITDA & Debt", xaxis_title="Year", yaxis_title="$M"))
        ]),
        dcc.Tab(label="Budget", children=[
            html.H3("Monthly P&L"),
            dcc.Graph(figure=go.Figure()
                .add_trace(go.Bar(x=budget["Month"], y=budget["Revenue"], name="Revenue"))
                .add_trace(go.Bar(x=budget["Month"], y=budget["Costs"], name="Costs"))
                .add_trace(go.Scatter(x=budget["Month"], y=budget["EBITDA"], name="EBITDA", mode="lines+markers"))
                .update_layout(title="Budget: P&L", xaxis_title="Month", yaxis_title="$M"))
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)