from pyclarify import ClarifyClient, DataFrame
from datetime import datetime
import pandas as pd

import orchest
import json
import sys
import os

data = orchest.get_inputs()
anomaly = data["alarm"][3]
item_name = orchest.get_step_param("item_name")

if not anomaly.empty:    
    credentials = os.environ["credentials"]
    client = ClarifyClient(credentials)
    
    data = DataFrame(series={item_name: anomaly["x"].tolist()}, times = anomaly["date"].tolist())
    response = client.insert(data)
    print(response.json())
    message = "New anomaly points in Clarify"
    
else:
    message = "No anomaly points, all good 💪"

orchest.output((message), name = "data")
