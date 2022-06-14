import pandas as pd
from orion import Orion
from converter import final_df

#trainer
hp = {
    'mlprimitives.custom.timeseries_preprocessing.time_segments_aggregate#1': {
        'interval': 43200 #changing time interval drastically affects anomaly detection. currently using half-day intervals.
    },
    "statsmodels.tsa.arima_model.Arima#1": {
            "steps": 1
    }
}
orion_model = Orion(pipeline="ARIMA", hyperparameters = hp)
detected_anomalies = orion_model.fit_detect(final_df)

anomalydata = pd.DataFrame(columns = ["timestamp", "value"])
for i in range(len(detected_anomalies.index)): #works for any number of anomalous segments
    start = detected_anomalies.iloc[i, 0]
    end = detected_anomalies.iloc[i, 1]
    anomalydata = anomalydata.append(final_df[final_df["timestamp"].between(start, end)])