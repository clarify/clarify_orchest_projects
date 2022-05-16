import orchest
from pyclarify import ClarifyClient, query
from datetime import datetime, timedelta
import os

item_id = orchest.get_step_param("item_id")
hours = orchest.get_step_param("hours")

print("Getting data from Clarify")
credentials = os.environ["clarify-credentials"]
client = ClarifyClient(credentials)

from_date = datetime.today() - timedelta(hours=hours) #days= 1, hours=1, minutes=5

filter = query.Filter(fields={"id": query.In(value=[item_id])})

response = client.select_items(filter = filter, not_before = from_date, before = datetime.today(), include_metadata = False)
df = response.result.data.to_pandas().drop_duplicates()

item_mt = client.select_items(filter = filter, include_metadata = True)
item_name = item_mt.result.items[item_id].name

orchest.output((df, item_name, hours, item_id), name = "response")

print("Success!")