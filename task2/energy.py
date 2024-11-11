import pandas as pd
csv1=pd.read_csv('task2/used_csv/totenergy.csv')
csv2=pd.read_csv('task2/used_csv/energysource.csv')
solar_percent=list(csv2['Electricity from solar - TWh']/csv1['Total Energy'])
newcsv=pd.DataFrame({
    'Country':csv1['Country'], 
    'Total Energy':csv1['Total Energy'],

    'Electricity from bioenergy - TWh':csv2['Electricity from bioenergy - TWh'],
    'Bioenergy Percentage':list(csv2['Electricity from bioenergy - TWh']/csv1['Total Energy']),

    'Electricity from coal - TWh':csv2['Electricity from coal - TWh'] ,
    'Coal Percentage':list(csv2['Electricity from coal - TWh']/csv1['Total Energy']),

    'Electricity from gas - TWh':csv2['Electricity from gas - TWh'] ,
    'Gas Percentage':list(csv2['Electricity from gas - TWh']/csv1['Total Energy']),

    'Electricity from hydro - TWh':csv2['Electricity from hydro - TWh'],
    'Hydro Percentage': list(csv2['Electricity from hydro - TWh']/csv1['Total Energy']),

    'Electricity from nuclear - TWh':csv2['Electricity from nuclear - TWh'] ,
    'Nuclear Percentage': list(csv2['Electricity from nuclear - TWh']/csv1['Total Energy']),

    'Electricity from oil - TWh':csv2['Electricity from oil - TWh'] ,
    'Oil Percentage':list(csv2['Electricity from oil - TWh']/csv1['Total Energy']),

    'Electricity from solar - TWh':csv2['Electricity from solar - TWh'] ,
    'Solar Percentage': solar_percent,

    'Electricity from wind - TWh':csv2['Electricity from wind - TWh'],
    'Wind Percentage':list(csv2['Electricity from wind - TWh']/csv1['Total Energy']),

})

newcsv.to_csv('task2/energy1.csv', index=False)