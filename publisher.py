import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as plt
from converter import final_df
from trainer import anomalydata

fig = go.Figure()

# add the main values to the figure
fig.add_trace(go.Scatter(x = final_df['timestamp'], y = final_df['value'],   #blue line is original data over time
                             mode = 'lines',
                             marker =dict(color='blue'),
                             name = 'original_signal'))
fig.add_trace(go.Scatter(x = anomalydata['timestamp'], y = anomalydata['value'], mode = 'markers',
                             marker = dict(color='red'),
                             name = 'detected_anomaly'))
#fig.show() #graph figure with discrete anomalies highlighted in red
st.plotly_chart(fig)