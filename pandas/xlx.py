import pandas as pd
df = pd.read_csv("C:\\Users\\sahil\\OneDrive\\Desktop\\Python\\Python\\pandas\\country.csv")
ser = pd.Series(df['Name'])
print(ser)
ser = pd.DataFrame(df[['Name','Age','Country']])
print(ser)
