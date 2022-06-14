import requests
from datetime import datetime
import csv
import pandas as pd
from pandas.io.json import json_normalize
import json

#converter script
api = open("api.txt", "r")
api_key = api.readline()
data_json = requests.get(api_key).json()
raw_df = pd.DataFrame(data_json)
time = api.readline() #read from the api file, time will be first a string representation of the name of the "time" column in the API call
value = api.readline() #read from the api file, value will be first a string representation of the name of the "value" column in the API call

#might need try / except blocks but you can check online for advice on converters
#the difficult thing will be finding dates / times and the one metric you care about in the timeseries, then making it into a 2 column df

standardized_time = raw_df[["close","date"]] #remember that datetime needs to be changed to a variable that represents the time column
standardized_time["datetime"] = standardized_time["date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
standardized_time["datetime"] = pd.to_timedelta(standardized_time["datetime"])
standardized_time["datetime"] = standardized_time["datetime"].dt.total_seconds()
final_df = pd.DataFrame({"timestamp":standardized_time["datetime"], "value": standardized_time["close"]}) #this line will need to be edited to change datetime and close, but is important

#lastly the final dataframe needs to be sent to trainer.py to train the model