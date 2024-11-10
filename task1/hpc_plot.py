import pandas as pd
import plotly.express as px


file_path = 'task1/TOP500_202406.xlsx'
data = pd.read_excel(file_path, sheet_name='63')

site_data = data[['Rank', 'Name', 'Site', 'Country', 'Computer', 'Year', 'Total Cores', 'Rmax [TFlop/s]', 'Rpeak [TFlop/s]']].head(500)

df = pd.read_csv('task1/coordinate.csv')

site_data['Latitude'] = df['Lat']
site_data['Longitude'] = df['Lon']

site_data_filtered = site_data.dropna(subset=['Latitude', 'Longitude'])

def assign_color_category(rmax):
    if rmax < 5030:
        return 'Low (<5030 Rmax [TFlop/s])'
    elif 5030 <= rmax < 10060:
        return 'Medium (5030-10060 Rmax [TFlop/s])'
    else:
        return 'High (>10060 Rmax [TFlop/s])'

site_data_filtered['HPC Category'] = site_data_filtered['Rmax [TFlop/s]'].apply(assign_color_category)

def assign_marker_size(rmax_category):
    if rmax_category == 'Low (<5030 Rmax [TFlop/s])':
        return 1
    elif rmax_category == 'Medium (5030-10060 Rmax [TFlop/s])':
        return 2
    else:
        return 3

site_data_filtered['Marker Size'] = site_data_filtered['HPC Category'].apply(assign_marker_size)

fig = px.scatter_geo(site_data_filtered,
                     lat='Latitude',
                     lon='Longitude',
                     title='Geographic Distribution of Top 500 High Performance Computers',
                     projection='natural earth',
                     color='HPC Category',
                     hover_name='Name',
                     hover_data=['Site','Rank', 'Rmax [TFlop/s]', 'Country'],
                     color_discrete_map={
                         'Low (<5030 Rmax [TFlop/s])': 'red',
                         'Medium (5030-10060 Rmax [TFlop/s])': 'yellow',
                         'High (>10060 Rmax [TFlop/s])': 'green'
                     },
                     size='Marker Size',
                     size_max=15)

fig.write_image("task1/geographic_distribution.png", width=1920, height=1080, scale=2)
fig.show()