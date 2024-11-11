import pandas as pd
co2_emmision=pd.read_csv('task2/CO2_emission.csv')

name=(pd.read_csv('task1/HPC_power.csv'))['Name']
maxpower=(pd.read_csv('task1/HPC_power.csv'))['Total_Power (kW)']
avgpwoer=(pd.read_csv('task1/HPC_power.csv'))['Average_Power(kW)']
country=(pd.read_csv('task1/HPC_power.csv'))['Country']
outpath_max='task2/max_CO2_Emission_by_HPCs.csv'
outpath_avg='task2/avg_CO2_Emission_by_HPCs.csv'
energy=pd.read_csv('task2/energy1.csv')
percent={'Bio':energy['Bioenergy Percentage'], 
         'Coal':energy['Coal Percentage'], 
         'Gas':energy['Gas Percentage'], 
         'Hydro':energy['Hydro Percentage'], 
         'Nuclear':energy['Nuclear Percentage'],
         'Oil':energy['Oil Percentage'],
         'Solar':energy['Solar Percentage'],
         'Wind':energy['Wind Percentage']
         }
countryenergy=list(energy['Country'])



totalemission=pd.DataFrame({
        'Name':name,
        'Emission from Bioenergy (gCO2/h)':[maxpower[i]*percent['Bio'][j]*co2_emmision['gCO2e/kWh'][0] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],
        'Emission from Coal (gCO2/h)':[maxpower[i]*percent['Coal'][j]*co2_emmision['gCO2e/kWh'][1] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],
        'Emission from Gas (gCO2/h)':[maxpower[i]*percent['Gas'][j]*co2_emmision['gCO2e/kWh'][2] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],
        'Emission from Hydro (gCO2/h)':[maxpower[i]*percent['Hydro'][j]*co2_emmision['gCO2e/kWh'][3] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],
        'Emission from Nuclear (gCO2/h)':[maxpower[i]*percent['Nuclear'][j]*co2_emmision['gCO2e/kWh'][4] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],
        'Emission from Oil (gCO2/h)':[maxpower[i]*percent['Oil'][j]*co2_emmision['gCO2e/kWh'][5] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],
        'Emission from Solar (gCO2/h)':[maxpower[i]*percent['Solar'][j]*co2_emmision['gCO2e/kWh'][6] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],
        'Emission from Wind (gCO2/h)':[maxpower[i]*percent['Wind'][j]*co2_emmision['gCO2e/kWh'][7] for i in range (len(maxpower)) for j in range (len(percent['Bio'])) if country[i]==countryenergy[j]],


})
totalemission['Total (gCO2/h)'] = totalemission[
    [
        'Emission from Bioenergy (gCO2/h)',
        'Emission from Coal (gCO2/h)',
        'Emission from Gas (gCO2/h)',
        'Emission from Hydro (gCO2/h)',
        'Emission from Nuclear (gCO2/h)',
        'Emission from Oil (gCO2/h)',
        'Emission from Solar (gCO2/h)',
        'Emission from Wind (gCO2/h)'
    ]
].sum(axis=1)


totalemission.to_csv(outpath_max,index=False)