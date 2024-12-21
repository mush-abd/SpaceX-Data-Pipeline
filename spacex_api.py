import requests
import pandas as pd

# response = requests.get('https://api.spacexdata.com/v4/launches')
# data = response.json()
# print(data)

url = 'https://api.spacexdata.com/v4/launches'

df = pd.read_json(url)

print(df.head())
print(df.dtypes)

# df = pd.DataFrame(data)
columns = df.columns
print(columns)

# print(df)
# print(df.head(5))