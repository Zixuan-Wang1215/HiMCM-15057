import pandas as pd
import plotly.express as px

file_path = 'task1/TOP500_202406.xlsx'
data = pd.read_excel(file_path, sheet_name='63')

site_data = data[['Rank', 'Name', 'Site', 'Country', 'Power (kW)', 'Total Cores', 'Rmax [TFlop/s]', 'Rpeak [TFlop/s]','Computer', 'Year']].head(500)

df = pd.read_csv('task1/coordinate.csv')

site_data['Latitude'] = df['Lat']
site_data['Longitude'] = df['Lon']

output_path = 'task1/top500_HPCs.csv'
site_data.to_csv(output_path, index=False)