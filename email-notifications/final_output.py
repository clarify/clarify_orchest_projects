import orchest

data = orchest.get_inputs()
anomaly = data["data"]
message = data["message"]
print(anomaly, "\n", message)
