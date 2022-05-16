import orchest
from pyclarify import ClarifyClient, query
from datetime import datetime, timedelta
import os

print("Getting data from Clarify")
item_id = orchest.get_step_param("item_id")

credentials = os.environ["clarify-credentials"]
client = ClarifyClient(credentials)

ts_start = orchest.get_step_param("from")
get_all_data = orchest.get_step_param("get_all_data")

filter = query.Filter(fields={"id": query.In(value=[item_id])})

if get_all_data:
    response = client.select_items(filter = filter, not_before = ts_start, before = datetime.today(), include_metadata = False)
    df = response.result.data.to_pandas().drop_duplicates()
    orchest.output((df), name = "response")

else:
    orchest.output(("None"), name = "response")
