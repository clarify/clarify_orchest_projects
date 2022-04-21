import orchest
from pyclarify import ClarifyClient
from datetime import datetime, timedelta
import os

print("Getting data from Clarify")
item_id = orchest.get_step_param("item_id")

credentials = os.environ["clarify-credentials"]
client = ClarifyClient(credentials)

ts_start = orchest.get_step_param("from")
get_all_data = orchest.get_step_param("get_all_data")

if get_all_data:
    response = client.select_items_data(ids = [item_id], not_before = ts_start, before = datetime.today())
    df = response.result.data.to_pandas().drop_duplicates()
    orchest.output((df), name = "response")

else:
    orchest.output(("None"), name = "response")
