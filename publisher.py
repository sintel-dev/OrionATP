import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as plt
import streamlit.components.v1 as components
from converter import final_df
from converter import selected
from trainer import detected_anomalies
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
st.header("Building the Pipeline")
st.markdown("Orion requires the data to be formatted in a very specific way, with the two columns of the dataframe being labelled 'timestamp' and 'value.' I set up the data to fit this format, then build a pipeline that doesn't vary much from the default ARIMA pipeline that's preprogrammed into the Orion library.")
st.dataframe(selected)

st.header("Detecting Anomalies")
st.markdown("Once the Orion pipeline is constructed, I fit the model to the data to train it and predict anomalous segments. The anomaly data is output into a dataframe representing the start and end of the anomalous sequence. Using a for loop, I split the sequence back into its original discrete data points that make it up in order to graph more effectively.")

st.dataframe(detected_anomalies)

st.dataframe(anomalydata)

st.header("Graphing the Data")
st.markdown("Finally, I graph the data. I still need to familiarize myself with plotly to create more effective graphs, but this basic graph seems to work for now. Discrete anomalous points are highlighted with red dots, while the timeseries data is graphed over time with the blue line.") 

st.plotly_chart(fig)

st.header("Conclusions")

st.markdown("It's obviously difficult to draw any sort of conclusions based on just this data set, but it seems like the Orion ARIMA pipeline is detecting anomalous segments during certain times of drastic increase in price. Obviously this script will change based on the Orion model used and the data set. There's also far too many variables that weren't taken into account for us to be able to draw any definitive conclusions about causation based off this data.")
