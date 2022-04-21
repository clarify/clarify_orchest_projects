import pandas as pd
import numpy as np
import orchest
import json

from utils import get_shared_dict
global_dict = get_shared_dict()

data = orchest.get_inputs()
results = data["anomaly"]
anomaly = results[0]
item_name = results[1]
number_hours = results[2]
item_id = results[3]

if number_hours == 1:
    hours = "hour" 
else:
    hours = "hours"

"""
if anomaly.empty and global_dict['alarm_flag'] == True:
    # Alarm reset
    print("Alarm reset")
    global_dict['alarm'] = 0
    global_dict['alarm_flag'] = False
    
    # email
    subject = "Anomaly Detected"
    html = # your body email
    
    maximum = 0
    plot = False
"""

if not anomaly.empty:
    
    maximum = max(anomaly["x"])
    plot = True
    anom_number = len(anomaly.index)
    
    if anom_number == 1:
        anomalies = "anomaly was"
    else:
        anomalies = "anomalies were"

    if global_dict['alarm_flag'] == False:
        # First alarm 
        print("First alarm ")
        global_dict['alarm'] = 1
        global_dict['alarm_flag'] = True
        
        # email
        subject = "Anomaly Detected"

        html = """\
        <html>
          <body>
            <p>In the last """+ str(number_hours)+""" """ +str(hours)+""" """ +str(anom_number)+""" """+str(anomalies)+""" found in """+str(item_name)+""".<br>
               View in <a href="https://clarifyapp.clarify.io/login">Clarify</a>.
            </p>
          </body>
        </html>
        """

    elif global_dict['alarm_flag'] == True:
        # Still alarm 
        print("Still alarm")
        global_dict['alarm'] = 1
        global_dict['alarm_flag'] = True
        
        # email
        subject = "Anomaly Detected"

        html = """\
        <html>
          <body>
            <p>In the last """+ str(number_hours)+""" """ +str(hours)+""" """ +str(anom_number)+""" more """+str(anomalies)+""" found in """+str(item_name)+""".<br>
               View in <a href="https://clarifyapp.clarify.io/login">Clarify</a>.
            </p>
          </body>
        </html>
        """

else:
    print("Everything is fine :)")
    subject = ""
    html = ""
    maximum = 0
    plot = False
    
orchest.output((subject, html, maximum, anomaly, plot, item_id), name = "alarm")
