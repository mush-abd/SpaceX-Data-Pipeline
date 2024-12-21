import requests
import pandas as pd

response = requests.get('https://api.spacexdata.com/v4/launches')
data = response.json()
# print(data)

df = pd.DataFrame(data)
columns = df.columns
print(columns)

# print(df)
# print(df.head(5))