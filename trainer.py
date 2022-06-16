import json
import pandas as pd
from orion import Orion
from converter import final_df


#trainer
json_pipeline = open("pipeline.json", "r")
pipeline = json.load(json_pipeline)

json_hyperparameters = open("hyperparameters.json", "r")
hp = json.load(json_hyperparameters)

orion_model = Orion(pipeline="ARIMA", hyperparameters = hp)
detected_anomalies = orion_model.fit_detect(final_df)

anomalydata = pd.DataFrame(columns = ["timestamp", "value"])
for i in range(len(detected_anomalies.index)): #works for any number of anomalous segments
    start = detected_anomalies.iloc[i, 0]
    end = detected_anomalies.iloc[i, 1]
    anomalydata = anomalydata.append(final_df[final_df["timestamp"].between(start, end)])