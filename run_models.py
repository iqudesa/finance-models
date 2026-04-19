import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title='Finance Pro', layout='wide')

st.markdown('''
<div style='background:linear-gradient(90deg,#1e3a8a,#3b82f6);padding:1.5rem;border-radius:1rem;text-align:center;color:white;'>
<h2>Finance PRO Dashboard</h2>
</div>
''', unsafe_allow_html=True)

DATA_DIR = Path(__file__).parent

@st.cache_data
def load_excel(name):
    return pd.read_excel(DATA_DIR / f'{name}.xlsx')

tab1, tab2, tab3 = st.tabs(['DCF', 'LBO', 'Budget'])

with tab1:
    df = load_excel('dcf')
    st.dataframe(df, use_container_width=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Year'], y=df['FCF'], name='FCF'))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['PV'], name='PV', line=dict(color='orange')))
    fig.update_layout(title='DCF: FCF vs PV', xaxis_title='Year', yaxis_title='$M')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    df = load_excel('lbo')
    st.dataframe(df, use_container_width=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Year'], y=df['EBITDA'], name='EBITDA'))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Net Debt'], name='Net Debt', line=dict(color='red')))
    fig.update_layout(title='LBO: EBITDA & Debt', xaxis_title='Year', yaxis_title='$M')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    df = load_excel('budget')
    st.dataframe(df, use_container_width=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Month'], y=df['Revenue'], name='Revenue'))
    fig.add_trace(go.Bar(x=df['Month'], y=df['Costs'], name='Costs'))
    fig.add_trace(go.Scatter(x=df['Month'], y=df['EBITDA'], name='EBITDA', mode='lines+markers'))
    fig.update_layout(title='Budget: P&L', xaxis_title='Month', yaxis_title='$M')
    st.plotly_chart(fig, use_container_width=True)

st.caption('Finance Models | Mock Data')
