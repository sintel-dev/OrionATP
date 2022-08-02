import json
import pandas as pd
from orion import Orion
from acquirer import final_df
from acquirer import original_time


#trainer
json_pipeline = open("pipeline.json", "r")
pipeline = json.load(json_pipeline)

json_hyperparameters = open("hyperparameters.json", "r")
hp = json.load(json_hyperparameters)

#if (no saved file):
orion_model = Orion(pipeline=pipeline, hyperparameters = hp)
# else:
# orion_model = Orion.load(INSERT_PICKLE_PATH)
# the above code, while not yet implemented due to bugtesting, allows for the user to access a previously created Orion instance 
# and update it with the new data instead of retraining the entire model.
detected_anomalies = orion_model.fit_detect(final_df)

anomalydata = pd.DataFrame(columns = ["timestamp", "value"])
for i in range(len(detected_anomalies.index)): #works for any number of anomalous segments
    start = detected_anomalies.iloc[i, 0]
    end = detected_anomalies.iloc[i, 1]
    anomalydata = anomalydata.append(original_time[original_time["seconds"].between(start, end)])
