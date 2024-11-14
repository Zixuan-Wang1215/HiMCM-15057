import pandas as pd

file_path = 'task1/TOP500_202406.xlsx'
data = pd.read_excel(file_path, sheet_name='63')

site_data = data[['Rank', 'Name', 'Country', 'Rmax [TFlop/s]', 'Power (kW)']].head(500)
dropna = site_data.dropna(subset=['Power (kW)'])

tflops = list(dropna['Rmax [TFlop/s]'])
power = list(dropna['Power (kW)'])

avg_power = [
    power[i] * (0.7 if tflops[i] >= 10060 else 0.6 if tflops[i] >= 5030 else 0.5)
    for i in range(len(dropna['Name']))
]

full_energy = [p * 31536000 for p in power]
avg_energy = [ap * 31536000 / 36000 for ap in avg_power]

print(len(avg_energy))
print(len(full_energy))

df = pd.DataFrame({
    'Name': dropna['Name'],
    'Country': dropna['Country'],
    'Rmax [TFlop/s]': dropna['Rmax [TFlop/s]'],
    'Total_Power (kW)': dropna['Power (kW)'],
    'Average_Power (kW)': avg_power,
    'Full_Energy (J/year)': full_energy,
    'Average_Energy (kWh/year)': avg_energy
})

df.to_csv('task1/HPC_power.csv', index=False)




